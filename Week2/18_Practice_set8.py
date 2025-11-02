# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
  if a>b and a>c:
    return a 
  elif b>a and b>c:
    return b
  elif c>a and c>b:
    return c
a = 2
b = 6
c = 4

print(greatest(a,b,c))

# 2. Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(f):
  return 5 *(f-32)/9
f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

# 3. How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c", end = "")
print("d")

# 4. Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
  if n==1:
    return 1
  return sum(n-1) + n
print(sum(8))

# 5. Write a python function to print first n lines of the following pattern:
'''***
   **  for n = 3
   *
   '''

def pattern(n):
  if n==0:
    return 
  print("*" * n)
  pattern(n-1)

pattern(3)

#  6. Write a python function which converts inches to cms.
def inch_to_cms(inch):
  return inch * 2.54
n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")


# 7. Write a python function to remove a given word from a list an strip it at the same time.
def rem(l, word):
  n =[]
  for item in l:
    if (item != word):
      n.append(item.strip(word))
  return n
l = ['Ajay', 'Divya', 'Rohit', 'Ruhi', 'it']
print(rem(l, 'it'))

# 8. Write a python function to print multiplication table of a given number.
def multiply(n):
  for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
  
multiply(5)