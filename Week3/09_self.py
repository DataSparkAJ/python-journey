class Employee:
  language = "Py" # This is a class attribute
  salary = 1200000

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")

  @staticmethod
  def greet():
    print("Good morning!")

ajay = Employee()
ajay.name = "Ajay" # This is an instance attribute
ajay.greet()
ajay.getInfo()
# Employee.getInfo(ajay)

