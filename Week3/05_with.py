f = open('file.txt')
data = f.read()
print(data)
f.close()

# The same can be written using with statement like this:
with open("file.txt") as f:
  print(f.read())

# We don't have to explicitly close the file