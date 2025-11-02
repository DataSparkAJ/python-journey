marks = {'Ajay': 100,
         'Suraj': 56,
         'Mohan': 22,
         0: 'Ajay'}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({'Ajay': 99, 'Renu': 56})
# print(marks)

print(marks.get('Ajay1')) # Prints None
print(marks['Ajay1']) # Return an error
