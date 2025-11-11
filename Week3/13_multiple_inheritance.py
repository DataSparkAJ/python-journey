class Employee:
  name = "default Name"
  company = "ITC"
  def show(self):
    print(f"The name is {self.name} and the company is {self.company}")

class Coder:
  language = "Python"
  def printLanguages(self):
    print("Out of all languages. Here is your language: {self.language}")  

class Programmer(Employee, Coder):
  company = "ITC Infotech"
  def showLanguage(self):
     print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()
b.showLanguage()
b.printLanguages()
b.show()

