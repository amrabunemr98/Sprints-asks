#!/bin/bash

# Variables for the remote server that will perform backup and restore operations
export server_username='ubuntu'    # Remote server's username
export server_ip='54.151.87.144'  # Remote server's IP address
export server_key='/home/abu-nemr/task-bash.pem' # Path to the private key file for accessing the server

# Function to validate the parameters passed to the backup.sh script
validate_backup_params() {
    # Check if exactly 4 arguments are provided to the script
    if [ $# -ne 4 ]; then
        # Print usage instructions if incorrect arguments are provided
        echo "Usage: $0 source_directory backup_directory encryption_key days_threshold"
        echo "1- source_directory: The path of the directory to be backed up."
        echo "2- backup_directory: The destination directory on the remote server where the backup will be stored."
        echo "3- encryption_key: The key used to encrypt the backup directory."
        echo "4- days_threshold: The number of days (n) to consider when backing up files modified within the last n days."
        exit 1  # Exit with an error code
    fi

    # Store the provided arguments in variables for easier reference
    source_directory="$1"    
    backup_directory="$2"
    encryption_key="$3"
    days_threshold="$4"

    # Check if the source directory exists locally
    if [ ! -d "$source_directory" ]; then
        echo "Error: $source_directory does not exist. Please ensure you enter the correct directory."
        exit 1
    fi

    # Check if the backup directory exists on the remote server
    ssh_check_result=$(ssh -i $server_key $server_username@$server_ip "[ -d '$backup_directory' ] && echo 'exists' || echo 'notexists'")

    # If the backup directory does not exist, create it on the remote server
    if [ "$ssh_check_result" = "notexists" ]; then
        echo "$backup_directory does not exist on the remote server. Creating it..."
        ssh -i $server_key $server_username@$server_ip "sudo mkdir -p '$backup_directory' && sudo chown ubuntu:ubuntu '$backup_directory' && sudo chmod 775 '$backup_directory'"
        echo "$backup_directory is successfully created on the remote server."
    fi

    # Validate that the provided encryption key exists in the local GPG keyring
    if ! gpg --list-keys | grep -q "$encryption_key"; then
        echo "Error: GPG key '$encryption_key' not found. Please make sure to enter the correct key."
        exit 1
    fi

    # Check if the days_threshold is a valid positive integer
    if ! [[ "$days_threshold" =~ ^[1-9][0-9]*$ ]]; then
        echo "Error: Invalid number of days."
        exit 1
    fi   
}

# Function to perform backup
backup() {
    # Get the current date in DD_MM_YYYY format
    snapshot_date=$(date +"%d_%m_%Y")

    # Create a temporary local directory to store the modified files to be backed up
    backup_dir="${snapshot_date}"
    mkdir -p $backup_dir

    # Find files modified in the source directory within the last 'days_threshold' days
    modified_files=$(find "$source_directory" -type f -mtime -$days_threshold)

    # Check if there are any modified files to back up
    if [ -n "$modified_files" ]; then
        echo "Found modified files. Starting backup..."

        # Loop through the modified files
        for file in $modified_files; do
            subdir=$(dirname "$file")       # Get the subdirectory of the file
            dir_name=$(basename "$subdir") # Get the base name of the subdirectory
            file_name=$(basename "$file")  # Get the file name

            # Create a .tgz archive for the file and encrypt it
            tar -czf "${backup_dir}/${dir_name}_${file_name}_${snapshot_date}.tgz" -C "$subdir" "$file_name"
            gpg --encrypt --recipient "$encryption_key" "${backup_dir}/${dir_name}_${file_name}_${snapshot_date}.tgz"
            rm "${backup_dir}/${dir_name}_${file_name}_${snapshot_date}.tgz"  # Remove unencrypted .tgz file
        done

        # Create a combined tar archive of all encrypted files
        combined_tar="${backup_dir}/all_files_${snapshot_date}.tar"
        first_encrypted=0 # Flag to check the first file
        for encrypted_file in "${backup_dir}"/*.tgz.gpg; do
            file_name=$(basename "${encrypted_file%.tgz.gpg}") # Extract file name without extension
            if [ $first_encrypted -eq 0 ]; then
                tar -cf "$combined_tar" -C "$backup_dir" "$file_name.tgz.gpg"
                first_encrypted=1
            else
                tar -rf "$combined_tar" -C "$backup_dir" "$file_name.tgz.gpg"
            fi
        done

        # Compress and encrypt the combined tar file
        gzip "$combined_tar"
        gpg --encrypt --recipient "$encryption_key" "${combined_tar}.gz"
        rm "${combined_tar}.gz" # Remove uncompressed file

        # Clean up individual encrypted files
        rm "${backup_dir}"/*.tgz.gpg

        # Transfer the backup directory to the remote server
        scp -i $server_key -r ${backup_dir} $server_username@$server_ip:"$backup_directory"

        # Clean up the local backup directory after copying it
        rm -r "${backup_dir}"

    else
        # No modified files found
        echo "There are no modified files in $source_directory within the last $days_threshold day(s) to be backed up."
        rmdir $backup_dir
    fi
}


# Function to validate the parameters for the restore.sh script
validate_restore_params() {
    # Check if the script received the correct number of parameters
    if [ $# -ne 3 ]; then
        # Print usage instructions if incorrect arguments are provided
        echo "Usage: $0 backup_directory restored_directory decryption_key"
        echo "1- backup_directory: Path of the directory on the remote server that contains the backup files to restore."
        echo "2- restored_directory: Path of the directory where the backup should be restored."
        echo "3- decryption_key: Key used to decrypt the backup files."
        exit 1
    fi

    # Store the provided arguments in variables for easier reference
    backup_directory="$1"
    restored_directory="$2"
    decryption_key="$3"

    # Check if the backup directory exists on the remote server
    ssh_check_result=$(ssh -i $server_key $server_username@$server_ip "[ -d '$backup_directory' ] && echo 'exists' || echo 'notexists'")
    if [ "$ssh_check_result" = "notexists" ]; then
        echo "Error: Backup directory does not exist on the remote server. Please ensure you enter the correct directory."
        exit 1
    fi

    # Check if the restored directory exists locally, if not, create it
    if [ ! -d "$restored_directory" ]; then
        echo "Restored directory does not exist. Creating it..."
        mkdir -p $restored_directory
        echo "$restored_directory successfully created."
    fi

    # Validate that the provided decryption key exists in the local GPG keyring
    if ! gpg --list-keys "$decryption_key" > /dev/null 2>&1; then
        echo "Error: GPG key '$decryption_key' not found. Please ensure you enter the correct key."
        exit 1
    fi
}

# Function to restore backup files
restore() {
    # Create a temporary directory inside the restored directory for intermediate operations
    mkdir -p "$restored_directory/temp_restore"

    # Copy the backup files from the remote server to the temporary directory
    scp -i $server_key -r $server_username@$server_ip:"$backup_directory"/* "$restored_directory/temp_restore"

    # Check if files were successfully transferred
    if [ -z "$(ls -A "$restored_directory/temp_restore")" ]; then
        echo "Error: No files were transferred from the remote backup directory."
        exit 1
    fi

    # Decrypt and extract the backup files inside the temporary directory
    encrypted_files=("$restored_directory/temp_restore"/*.tar.gz.gpg) # Locate encrypted backup files
    if [ ${#encrypted_files[@]} -gt 0 ]; then
        for encrypted_file in "${encrypted_files[@]}"; do
            decrypted_file="${encrypted_file%.gpg}" # Remove the .gpg extension for the decrypted file
            # Decrypt the file using GPG
            if ! gpg --output "$decrypted_file" --decrypt --recipient "$decryption_key" "$encrypted_file"; then
                echo "Error: Decryption of file $encrypted_file failed."
                exit 1
            fi

            # Extract the contents of the decrypted tar.gz file
            tar -xzf "$decrypted_file" -C "$restored_directory/temp_restore"

            # Clean up by removing the decrypted tar file and the encrypted file
            rm "$decrypted_file" "$encrypted_file"
        done
    fi

    # Loop through the extracted files to handle any additional .tgz files
    for content in "$restored_directory/temp_restore"/*; do
        if [ -f "$content" ]; then
            decrypted_file="${content%.gpg}" # Remove .gpg extension for decryption
            if ! gpg --output "$decrypted_file" --decrypt --recipient "$decryption_key" "$content"; then
                echo "Error: Decryption of file $content failed."
                exit 1
            fi

            # Check if the decrypted file is a .tgz archive
            if [[ "$decrypted_file" == *.tgz ]]; then
                extraction_dir="${decrypted_file%.tgz}" # Create a directory name by removing .tgz
                mkdir -p "$extraction_dir"

                # Extract the contents of the .tgz file into the directory
                tar -xzf "$decrypted_file" -C "$extraction_dir"

                # Remove the extracted .tgz file
                rm "$decrypted_file" "$content"
            fi
        fi
    done

    # Move all extracted files from the temporary directory to the restored directory
    mv "$restored_directory/temp_restore"/* "$restored_directory"
    # Clean up by removing the temporary directory
    rmdir "$restored_directory/temp_restore"

    echo "Restore operation completed successfully."
}

# Uncomment below to run validate and backup/restore as needed:
# validate_backup_params "$@"
# backup
# validate_restore_params "$@"
# restore
