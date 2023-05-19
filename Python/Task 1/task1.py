def function():
    string = input("please enter word:")   # user enter any word as input in string
    string_list = list(string)             # convert string to list
    new_char = input("please enter new character:")  # user enter new char 
    index = int(input("please enter number of character you want to change:"))  # user enter number of char in index
    if index >= len(string_list): # check number of index = len size 
        print("index is not right")
    else:
        string_list[index] = new_char  # change old char to new char in word
        new_string = ''.join(string_list)   # convert list to string 
        print("new word:{}".format(new_string))


function()
