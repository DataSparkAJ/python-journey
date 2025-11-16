a= 89 # Global variable

def fun():
  global a
  a = 3
  print(a)

fun()
print(a)