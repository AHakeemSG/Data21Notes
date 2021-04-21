# # Determine if a word or a phrase is an isogram
#
# # An isogram (non-pattern word) is a word or phrase without a repeating letter,
# # However, spaces and hyphens are allowed to appear multiple times
#
# # Examples of isograms: lumberjacks, background, downstream, six-year-old
# # The word isograms, however, is not an isogram because the s repeats
#
# # Solution 1
# def check_isogram(words):
#     return len(words) == len(set(words.lower()))
#
#
# print(check_isogram("lumberjack"))
# print(check_isogram("perpetual"))
# print(check_isogram("abanoub"))
# print(check_isogram("greek"))
#
#
# # Solution 2
# def isogram(word):
#     clean_word = word.lower()
#     letter_list = []
#
#     for letter in clean_word:
#         if letter.isalpha():
#             if letter in letter_list:
#                 return False
#             letter_list.append(letter)
#
#     return True
#
#
# # Solution 3
# def isograms(string):
#     for item in string:
#         spaces = " "
#         hypthens = "-"
#         if string.count(item) > 1:
#             return False
#         elif string.count(item) > 1:
#             return True
#         else:
#             pass
#     return True
#
#
# abc = isograms("lumberjack")
# print(abc)
#
# bcd = isograms("greeks")
# print(bcd)
#
# name = isograms("abanoub")
# print(name)
#
# # Solution 4
#
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
#            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# phrase = input("Please enter your phease: \n")
# phrase_lower_case = phrase.lower_case = phrase.lower()
# for letter in letters:
#     letter_count = phrase_lower_case.count(letter)
#     if letter_count > 1:
#         print(f"The {phrase} is not an isogram.")
#         break
#     elif letter == "z":
#         print(f"The  {phrase} is an isogram.")
#
#
# Fizzbuzz
# num_input = input("What is the number you would like to input? \n")
# for n in number(range(0, 100)):
#     # output = ""
#     if x % 3 == 0 and x % 5 == 0:
#         print("Fizz Buzz")
#     elif x % 5 == 0:
#         print("Buzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     else:
#         print(x)
#
# # Solution 2
# num_input = input("What is the number you would like to input? \n")
# for x in range(1, 101):
#     if not x % 3:
#         if not x % 5:
#             print('Fizz Buzz')
#         else:
#             print('Fizz')
#     elif not x % 5:
#         print('Buzz')
#     else:
#         print(x)
#
# # Solution 3
# num_input = input("What is the number you would like to input? \n")
# for num in range(1, 101):
#     if num % 5 == 0 and num % 3 == 0:
#         print(num)
#         print("FIZZBUZZ")
#     elif num % 5 == 0:
#         print(num)
#         print("BUZZ")

# # Solution 4
# num_input = input("What is the number you would like to input? \n")
#
#
# def fizzbuzz(lower, higher):
#     result = []
#     for number in range(lower, higher):
#         if number % 3 == 0 and number % 5:
#             result.append("FizzBuzz")
#         elif number % 3 == 0:
#             result.append("Fizz")
#         elif number % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(number))
#     return result
#
#
# print(fizzbuzz(1, 31))

# Solution 5
from numbers import num_list  # Imported from another source i.e. numbers.py


num_input = input("What is the number you would like to input? \n")

for num in num_list:
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

