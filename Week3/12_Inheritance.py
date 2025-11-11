class Employee:
  name = "default name"
  salary = 1200000
  def show(self):
    print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#   company = "ITC Infotech"
#   def show(self):
#     print(f"The name is {self.name} and the salary is {self.salary}")

#   def showLanguage(self):
#     print(f"The name is {self.name} and he is good with {self.language} language")
  
class Programmer(Employee):
  salary = 1300000
  language = "Java"
  def showLanguage(self):
     print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.salary, b.salary)
