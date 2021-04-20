#
# # Defining variables
# variable_name = "Hello"
# a = 20
# b = 6.7
#
# # Printing variables
# print(a)
# print(variable_name)
# print(b)
# print (a + b)
#
# # data types
# print(type(a))
# print(type(b))
# print(type(variable_name))
#
# # user input
# print("What is your name")
# name = input()
# print("Hello" + name)
#
# # Another way for user input  - f string
# name = input("What is your name")
# print(f"Hello  {name}")
#
#
# Activity - ask for name, age, height, date
# name = input("  What is your name?")
# age = input("  What is your age?")
# height = input("  What is your height?")
# dob = input("  What is your date of birth")
#
# # Solution
# print(f"Hello {name}, you are {age} years old. you are {height} m tall. You date of birth is {dob}.")

# Slicing
# hi = "Hello World"
# print(hi[0:5])  # To get just hello
#
# # Return every second letter
# print(hi[0:12:2])  # The second number (2) allows to incement
#
# # Return the string backwards
# print(hi[::-1])
#
# # Upper case
# print(hi.upper())
#
# # Lower case
# print(hi.lower())
#
# # Capitalise String
# print(hi.capitalize())
#
# # Counts
# print(hi.count('l'))
#
# # Concatenation
# names = "abanoub"
# names2 = "hakeem"
# print(names + " " + names2)
#
# # Boolean
# a = True
# b = False
# print(a == b)
#
# hii = "Hello World"
# print(hii.isalpha())  # alpha numeric  - returns False because the space between words
#
# # print(hi.is) # type is and there is a lot of functions that come up such as isnumeric, isdigit etc
#
# print(hi.endswith('d'))
#
# x = 10
# y = 0
# print(bool(x)) # True because indicates there is value
# print(bool(y)) # False because 0 indicates no value
#
# # Bool - assigning to none
# z = None
# print(bool(z == None))
# print(bool(z == False))  # False not True


# # Lists - are mutable
# shopping_list = ["eggs", "milk", "bread"]  # Lists are created through square brackets
# print(shopping_list)
# print(shopping_list[0])  # 1st element slicing (eggs)
# print(shopping_list[0:-1])
# print(type(shopping_list))
#
# # replacing elements in a list
# shopping_list[0] = "chocolate"
# print(shopping_list)
#
#
# # Tuples - Tuples are imutatable
# shopping_tup = ("bread", "milk", "eggs")
# print(shopping_tup)


# Dictionaries - Set of keys and values (key value pairs)
# student_dict = {
#     "name": "Abanoub",
#     "stream": "data engineering",
#     "qualifications": ["BSc", "MSc"]
# }
#
# print(student_dict)
# print(student_dict["qualifications"][1])  # to access element 1 from qualifications list
#
# # changing values in dict
# student_dict["name"] = "ab"
# print(student_dict)
#
# # to view values in dict
# print(student_dict.values())
#
# # removing values in dict
# student_dict["qualifications"].remove("BSc")
# print(student_dict)
#
#
# # Sets
# car_parts = {"wheels", "steering wheel", "doors", "windows"}
# print(type(car_parts))
#
# # adding values to sets
# car_parts.add("headlights")
# print(car_parts)
#
# # removing values from sets
# car_parts.discard("doors")
# print(car_parts)


# Control flow - If statements, For loops, While loops

# IF statements
# age = 3
# if age > 18:
#     print("You are older than 18")
# else:
#     print("You are younger than 18")
#
# age2 = 60
# if age2 > 18:
#     print("You are older than 18")
# elif age2 > 50:
#     print("You are older than 50")
# else:
#     print("You are younger than 18")


# Loops
# list_data = [1, 2, 3, 4, 5, 6, 7, 8,]
#
# for data in list_data:
#     print(data)

# em_list = [1, 2, 3], [2, 3, 4]  # embedding list or list of lists
# for data in em_list:
#     print(data)
#     for num in data:
#         print(num)

# # While loop
# xx = 0
# while xx < 10:
#     print("this is true")
#     if xx == 4:
#         break  # break command breaks the loop when reached assigned value
#     xx += 1  # creating an increment then reassigning to xx


user_prompt = True
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer as a digit")
