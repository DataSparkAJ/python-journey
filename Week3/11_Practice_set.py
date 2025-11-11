# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
  company = 'Microsoft'
  def __init__(self, name, salary, pin):
    self.name = name
    self.pin = pin
    self.salary = salary

p = Programmer('Ajay', 1200000, 244121)
print(p.name, p.pin, p.salary)
r = Programmer('Rohit', 1200000, 244121)
print(r.name, r.pin, r.salary)

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
  def __init__(self, n):
    self.n = n
    
  def square(self):
    print(f"The square is {self.n*self.n}")
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")
  def sqrt(self):
    print(f"The square root is {self.n**1/2}")

c = Calculator(5)
c.square()
c.cube()
c.sqrt()

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class Demo:
  a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute

# 4. Add a static method in problem 2, to greet the user with hello.
class Calculator:
  def __init__(self, n):
    self.n = n
    
  def square(self):
    print(f"The square is {self.n*self.n}")
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")
  def sqrt(self):
    print(f"The square root is {self.n**1/2}")
  @staticmethod
  def hello():
    print("Hello there !")

c = Calculator(5)
c.hello()
c.square()
c.cube()
c.sqrt()

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:

  def __init__(self, trainNo):
    self.trainNo = trainNo

  def book(self, fro, to):
    print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}.")

  def getStatus(self):
    print(f"Ticket is booked in train no: {self.trainNo} is running on time.")

  def getFare(self, fro, to):
    print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}.")

t = Train(12345)
t.book("Moradabad", "Delhi")
t.getStatus()
t.getFare("Moradabad", "Delhi")

# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
class Train:

  def __init__(slf, trainNo):
    slf.trainNo = trainNo

  def book(harry, fro, to):
    print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}.")

  def getStatus(self):
    print(f"Ticket is booked in train no: {self.trainNo} is running on time.")

  def getFare(self, fro, to):
    print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}.")

t = Train(12345)
t.book("Moradabad", "Delhi")
t.getStatus()
t.getFare("Moradabad", "Delhi")