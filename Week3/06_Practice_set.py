# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("poems.txt") as f:
  content = f.read()
  if "twinkle" in content:
    print("The word twinkle is present in the content.")
  else:
    print("The word twinkle is not present in the content.")

# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game():
  print("You are playing a game.")
  score = random.randint(1,100)
  # Fetch the hiscore
  with open("hiscore.txt") as f:
    hiscore = f.read()
    if hiscore != '':
      hiscore = int(hiscore)
    else:
      hiscore = 0
    print(f"Your score is {score}")
    # write the hiscore to the file
    if score > hiscore:
      with open('hiscore.txt','w') as f:
        f.write(str(score)) # can write only string value

game()

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
def generate_table(n):
  table = ''
  for i in range(1,11):
    table += f"{n} X {i} = {n*i}\n"
  with open(f"Tables/table_{n}.txt", 'w') as f:
    f.write(table)
  
for i in range(2,21):
  generate_table(i)

# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
word = 'Donkey'
with open("file.txt", 'r') as f:
  content = f.read()
  contentNew = content.replace(word , "#####")
with open("file.txt", 'w') as f:
  f.write(contentNew)

# 5. Repeat program 4 for a list of such words to be censored.
words = ['Donkey', 'ganda', 'bad']
with open("file.txt", 'r') as f:
  content = f.read()
for word in words:
  content = content.replace(word , "#"*len(word))
with open("file.txt", 'w') as f:
  f.write(content)

# 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open('log.txt') as f:
  content = f.read()
  if 'python' in content:
    print("Yes python is present.")
  else:
    print("No python is not present.")

# 7. Write a program to find out the line number where python is present from ques 6.
with open ("log.txt",'r') as f:
  lines = f.readlines()
  lineno = 1
  for line in lines:
    if 'python' in line:
      print(f"Yes python is present. Lineno: {lineno}")
      break
    lineno += 1
  else:
    print("No python is not present.")

# 8. Write a program to make a copy of a text file “this. txt”
with open('this.txt') as f:
  content = f.read()
with open('copy_this.txt', 'w') as f:
  f.write(content)

# 9. Write a program to find out whether a file is identical & matches the content of another file.
with open ('file.txt') as f:
  content1 = f.read()
with open ('poems.txt') as f:
  content2 = f.read()
if content1 == content2:
  print("Yes both files are identical.")
else:
  print("No both files are not identical.")

# 10. Write a program to wipe out the content of a file using python.
with open('copy_this.txt', 'w') as f :
  f.write('')

# 11. Write a python program to rename a file to “renamed_by_ python.txt.
import os
os.rename('old.txt', 'renamed by python')