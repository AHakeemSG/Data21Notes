# Try and except error handling

# function for opening
def open_and_print(file="order.text"):
    try:
        opened_file = open("order.txt", "r")
        file_line_list = opened_file.readlines()
        print(file_line_list)

        # For loop for removing the \n in the printed lists
        for line in file_line_list:
            print(line.rstrip('\n'))

        # Closing the file
        opened_file.close()

    except FileNotFoundError as errmsg:
        print("There has been an error opening your file!")
        print(errmsg)  # we can print out the error message
        # and the error message that you have written
    #    raise  # will bring back the exception that is captured


open_and_print("order.txt")


# Function for writing to a file
def write_to_file(order_item, file="order.txt"):
    try:
        with open(file, "a") as opened_file:
            opened_file.write(order_item + "\n")
    except FileNotFoundError:
        print("file cannot be found")
    except FileExistsError:
        print("file already exists")


# Using both of the functions to open the file and then write in it
write_to_file("Lasagna")
open_and_print()


# Below is a cleaner code solution for opening and reading a files, then writing files:
def open_and_print_file(file="order.txt"):
    try:
        with open(file, "r") as opened_file:  # "a" is for appending
            for line in opened_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print("file cannot be found")
    except FileExistsError:
        print("file already exists")


# function for writing a file
def write_to_file(order_item, file="order.txt"):
    try:
        with open(file, "a") as opened_file:
            for item in order_item:
                opened_file.write('\n' + item)
    except FileNotFoundError:
        print("file cannot be found")
    except FileExistsError:
        print("file already exists")


# Adding new words to the order.txt through a function that accepts multiple arguments
appended_list = ['tacos', 'cheeseburgers', 'steak', 'cocktails']
write_to_file(appended_list)
open_and_print_file("order.txt")
