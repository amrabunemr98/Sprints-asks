import csv
import datetime

print(" Hello Dear, Welcome in My Project of Contact Book")
current_date = datetime.datetime.now().strftime("%d%m%Y")  # Get the current date and time.
current_working_file = f"Contact book_{current_date}.csv"  # Create a file name for the current working file.


def import_original_data():  # Define a function to import the original data from the Contact Book.csv file.
    with open('Contact Book.csv', 'r') as original_file:  # Open the Contact Book.csv file in read mode.
        reader = csv.reader(original_file)  # Create a reader object to read the file.
        with open(current_working_file, 'w', newline='') as new_file:
            # Create a new file object for the current working file.
            adder = csv.writer(new_file)
            for row in reader:  # Write the rows from the original file to the new file.
                adder.writerow(row)


def export_updated_data():  # Define a function to export the updated data to the Contact Book.csv file.
    # This function exports the updated data to the Contact Book.csv file.
    # Open the current working file in read mode.
    with open(current_working_file, 'r') as new_file:
        # Create a reader object to read the file.
        reader = csv.reader(new_file)
        # Open the Contact Book.csv file in write mode.
        with open('Contact Book.csv', 'w', newline='') as original_file:
            # Create a writer object to write to the file.
            adder = csv.writer(original_file)
            # Write the rows from the current working file to the original file.
            for row in reader:
                adder.writerow(row)


def user_selection():  # Define a function to let the user select a method to perform.
    # Get the user's selection.
    selection = input(" Select Method You Want to Do in This List: 1-Create Data  2-Update Data  3-Delete Data : ")
    # Check if the user's selection is valid.
    if selection.isdigit():
        # If the user's selection is 1, call the user_input() function.
        if int(selection) == 1:
            user_input()
        elif int(selection) == 2:  # If the user's selection is 2, call the user_update() function.
            user_update()
        elif int(selection) == 3:  # If the user's selection is 3, call the user_delete() function.
            user_delete()
        else:  # If the user's selection is not 1, 2, or 3, print an error message.
            print(" It's Wrong Input Number of Method So Please Enter Right Number of Method ")
            user_selection()
    else:  # If the user's selection is not a digit, print an error message.
        print(" Please Enter a Valid Choice From List")
        user_selection()


def user_input():  # Define a function to let the user enter contact information.
    #  Create a flag to indicate whether the user wants to continue entering contact information.
    flag = 0
    x = int(input(" If You Want To: 1-Back to List  2-Continue Create Data : "))
    if x == 1:
        user_selection()
    elif x == 2:
        contact_name = input(" Please Enter Contact Name: ")
        contact_email = input(" Please Enter Contact Email: ")
        insert_date = datetime.datetime.now().strftime('%d-%m-%Y- %H:%M:%S')  # Get the current date and time.
        while flag == 0:  # Let the user enter the contact number.
            contact_number = input(" Please Enter Phone Number: ")
            if contact_number.isdigit():
                flag = 1
            else:
                print("Please Enter Correct Contact Number")
                flag = 0
        contact_address = input(" Please Enter Contact Address: ")
        # Save the contact information to a file.
        save_input(contact_name, contact_email, contact_number, contact_address, insert_date)
        print(" Your Data Has Been Submitted Successfully ")
        restart_apps()


def save_input(contact_name, contact_email, contact_number, contact_address, insert_date):
    # This function saves contact information to a file.
    with open('Contact Book.csv', 'a', newline='') as file:  # Open the `Contact Book.csv` file in append mode.
        add = csv.writer(file)  # Write the contact information to the file.
        add.writerow([contact_name, contact_email, contact_number, contact_address, insert_date])
    import_original_data()  # Import the original data from the `Contact Book.csv` file.
    export_updated_data()   # Export the updated data to the `Contact Book.csv` file.


def user_update():  # Define a function to update contact information.
    import_original_data()
    # Create a flag to indicate whether the user wants to continue updating contact information.
    flag = 0
    flag1 = 0
    while flag1 == 0:   # Let the user select the field to update
        search_field = input(" Enter Field You Want to Update: 1-Contact Name, 2-Contact Email, 3-Contact Number, "
                             "4-Contact Address, 5-Back to Home List : ")
        if search_field.isdigit():
            flag1 = 1
        else:
            print(" Please Enter Right Number of Choices")
            flag1 = 0
    if 0 < int(search_field) < 6:  # Check if the user's selection is valid.
        if int(search_field) == 5:  # If the user's selection is 5, call the user_selection() function.
            user_selection()
        search_email = input(" Please Enter Email of Contact You Want to Update: ")
        with open(current_working_file, 'r') as file:  # Get the current working file.
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:  # Find the row in the file that contains the contact information for the user.
            if row[1] == search_email:
                validation = 1
                break
            else:
                validation = 0
        if validation == 1:  # If the contact information is found, update the field with the new value.
            for row in rows:
                if row[1] == search_email:
                    if int(search_field) == 1:
                        new_value = input(" Please Enter New Value: ")
                        row[0] = new_value
                    elif int(search_field) == 2:
                        new_value = input(" Please Enter New Value: ")
                        row[1] = new_value
                    elif int(search_field) == 3:
                        while flag == 0:
                            new_value = input(" Please Input The New Contact Number: ")
                            if new_value.isdigit():
                                flag = 1
                            else:
                                print(" Please Enter Correct Contact Number! ")
                                flag = 0
                        row[2] = new_value
                    elif int(search_field) == 4:
                        new_value = input(" Please Enter New Value: ")
                        row[3] = new_value
            with open(current_working_file, 'w', newline='') as file:   # Write the updated data to the file.
                writer = csv.writer(file)
                writer.writerows(rows)
            print(" Contact Has Been Updated Successfully ")
            export_updated_data()
            restart_apps()  # Restart the application.
        else:
            print(" Please Enter Correct Email of Contact ")
            user_update()
    else:   # If the user's selection is not 1, 2, 3, 4, or 5, print an error message.
        print(" It's Wrong Input Number of Field So Please Enter Right Number of Field ")
        user_update()


def user_delete():  # Define a function to delete contact information.
    import_original_data()  # Import the original data from the Contact Book.csv file.
    x = int(input(" If You Want To: 1-Back to List  2-Continue Delete Data : "))
    if x == 1:
        user_selection()   # Let the user select the contact to delete.
    elif x == 2:
        search_email = input(" Please Enter Email of Contact You Want to Delete: ")
        with open(current_working_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            if row[1] == search_email:
                validation = 1
                break
            else:
                validation = 0
        if validation == 1:  # If the contact information is found, delete the row from the file.
            for row in rows:
                if row[1] == search_email:
                    rows.remove(row)
                with open(current_working_file, 'w', newline='') as file:  # Write the updated data to the file.
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print(" Contact Has Been Deleted Successfully ")
                export_updated_data()
                restart_apps()
        else:  # If the contact information is not found, print an error message.
            print(" It's Wrong Email So Please Enter Correct Email of Contact ")
            user_delete()


def restart_apps():  # Define a function to restart the application.
    # Let the user decide whether to restart the application.
    restart_app = input(" Do You Want To Do Anything Else?(Yes/No): ")
    if (restart_app == "Yes") | (restart_app == "yes"):   # If the user says yes, restart the application.
        user_selection()
    elif (restart_app == "No") | (restart_app == "no"):   # If the user says no, exit the application.
        print(" Thank You For Using Our Contact Book ")
        exit()


# Call the user_selection() function to start the application.
user_selection()
