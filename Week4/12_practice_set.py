# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
try:
  with open ("1.txt") as f:
    print(f.read())
except Exception as e:
  print(e)
try:
  with open ("2.txt") as f:
    print(f.read())
except Exception as e:
  print(e)
try:
  with open ("3.txt") as f:
    print(f.read())
except Exception as e:
  print(e)

print("Thank You!`1")

# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.
l = [1,2,3,4,5,6,7,8]
for index, item in enumerate(l):
  if index == 2 or index == 4 or index ==6:
    print(item)

# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
n = int(input("Enter a number: "))

table = [i*n for i in range(1,11)]
print(table)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
try:
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  print(a/b)
except ZeroDivisionError as v:
  print("Infinite")

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
with open("tables.txt", "a") as f:
  f.write(f"Table of {n}: {str(table)} \n")