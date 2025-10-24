# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print(f"Good Afternoon {name}!")

# Write a program to fill in a letter template given below with name and date
letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> '''

print(letter.replace("<|Name|>", "Ajay").replace("<|Date|>","19 October 2050"))

# Write a program to detect double space in a string.
name = "John is a good boy and  "
print(name.find("  "))

# Replace the double space from problem 3 with single spaces.
name = "John is a good  boy and  "
print(name.replace("  "," "))

# Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"

print(letter)