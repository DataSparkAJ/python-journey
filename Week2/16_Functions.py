# a = int(input("Enter your number"))
# b = int(input("Enter your number")) 
# c = int(input("Enter your number"))

# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number"))
# b = int(input("Enter your number")) 
# c = int(input("Enter your number"))

# average = (a + b + c)/3
# print(average)
# Functions Definition
def avg():
  a = int(input("Enter your number: "))
  b = int(input("Enter your number: ")) 
  c = int(input("Enter your number: "))

  average = (a + b + c)/3
  print(average)

avg() # Functions Call
print("Thank You!")
avg()
print("Thank You!")
avg()
avg()

# Quick Quiz: Write a program to greet a user with “Good day” using functions.
def goodDay():
  print("Good Day!")
goodDay()

# Functions with arguments 
def goodDay(name, ending):
   print("Good Day, " + name)
   print(ending)
goodDay("Ajay","Thank You!")
goodDay("Divya","Thanks!")

def goodDay(name, ending):
   print("Good Day, " + name)
   print(ending)
a = goodDay("Ajay","Thank You!")
print(a) # output None

def goodDay(name, ending):
   print("Good Day, " + name)
   print(ending)
   return "done"
a = goodDay("Ajay","Thank You!")
print(a) 

# default argument
def goodDay(name, ending = "Thank You!"): # it says if i provide you the value of ending take it otherwise use default value
   print(f"Good Day", {name})
   print(ending)
goodDay("Ajay") 

