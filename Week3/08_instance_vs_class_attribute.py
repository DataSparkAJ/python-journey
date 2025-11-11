class Employee:
  language = "Py" # This is a class attribute
  salary = 1200000

ajay = Employee()
ajay.language = "Javascript" # This is an instance attribute
print(ajay.salary, ajay.language)
