# Question 1

# Given a number, print that number the amount of time of its value

for i in range(1, 11):

    print(str(i) * i)

# Another solution
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in mylist:

    print(str(i) * i)


# Question 2

# given a string, print out every letter individually

string_given = "abanoub"

for i in string_given:
    print(i)


# Question 3

# Give 2 integers, return their product. If the product is greater than 1000, return their sum

int1 = 30
int2 = 20

product = int1 * int2
if product > 1000:
    print(int1 + int2)
else:
    print(product)


# Question 4

# Given a list of numbers, iterate it and print out only those number that are divisible by 5

my_list = [10, 20, 33, 46, 55]

for i in my_list:
    if i % 5 == 0:
        print(i)



# Question 5

# given a string, how many times has a sub string has occured. Count how many times emma has appeared

string_example = "emma is a good developer, emma is a writer"

emma = string_example.count("emma")
print(emma)


# another solution

string_example = "emma is a good developer, emma is a writer"
count = 0
for i in range(len(string_example) - 1):
    count += string_example[i:i + 4] == "emma"

print(count)


# Question 5

# return the max int

int4 = 444
int5 = 555


def maxi(int4, int5):
   if int4 >= int5:
       return int4
   elif int5 >= int4:
       return int5


print(maxi(int4, int5))


# question 6

# given a number, count the total number of digits

int6 = 75869

print(len(str(int6)))

# Another solution

count = 0
while int6 != 0:
    int6 //=10
    count +=1

print(count)


# Question 7

# Display the numbers -10 to -1 using a for loop

for i in range(-10, 0, 1):   # the last arg indicates the step
    print(i)





