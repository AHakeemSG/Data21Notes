# Lambda

# Comparison of lambda to functions

# Function
def addition(num1, num2):
    return num1 + num2


# print(addition(2, 3))

# transforming function to lambda expression
add = lambda num1, num2: num1 + num2
print(add(2, 3))

# map expression - takes in a function and an iterable

# Another example of lambda expression using mapping
saving = [234, 555, 674, 78]
bonus = list(map(lambda x: x * 1.1, saving))  # apply a 10% bonus to those savings through function

print(bonus)

# Another solution to the same bonus question
saving = [234, 555, 674, 78]
bonus = []


# Bonus function
def bonus_function():
    for i in saving:
        increased_value = i * 1.10
        print(increased_value)


bonus_function()
