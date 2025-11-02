print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1, 6):
  print(i)

# while loops
i = 1
while(i<6):
  print(i)
  i+=1

# Write a program to print the content of a list using while loops.
l = ['Ajay', False, 'This', 'For', 'While', 'Range', 0]
i = 0
while i < len(l):
  print(l[i])
  i+=1

# for loops
for i in range(4):
  print(i)

# for loop iterate
l = [2,4,5,7,8,9,4]
for i in l:
  print(i)

s = 'Ajay'
for i in s:
  print(i)

# for loop with else
l = [1,3,2]
for item in l:
  print(item)
else:
  print('Done') # this is printed when the loop exhausts

# break and continue
for i in range(100):
  if i == 41:
    break # Exit the loop right now
  print(i)

for i in range(100):
  if i == 41:
    continue # Skip this iteration
  print(i)

# pass
for i in range(300):
  pass # it constructs to do nothing

i = 0
while i < 45:
  print(i)
  i+=1