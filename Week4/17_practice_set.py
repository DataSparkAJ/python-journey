# 1. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”
name = input("Enter your name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
print(s)

# 2. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
table = [str(7*i) for i in range (1,11)]

s = "\n".join(table)
print(s)

# 3. Write a program to filter a list of numbers which are divisible by 5.
l = [5,3,10,10,55,20,35,89,45]

divisible5 = lambda x: x%5 == 0
print(list(filter(divisible5,l)))

# 4. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l = [234,23,57,786,456,345]

greater = lambda a,b: a if a>b else b
print(reduce(greater,l))

