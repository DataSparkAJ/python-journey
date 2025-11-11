class Employee:
  language = "Py" # This is a class attribute
  salary = 1200000

ajay = Employee()
ajay.name = "Ajay" # This is an instance attribute
print(ajay.name, ajay.salary, ajay.language)

rohit = Employee()
rohit.name = "Rohit"
print(rohit.name, rohit.language, rohit.salary)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class 

