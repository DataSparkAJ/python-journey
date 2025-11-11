class Dog:
  a = 0
  @classmethod
  def show(cls):
    print(f"The class attribute of a is {cls.a}")

d = Dog()
d.a = 21
d.show()