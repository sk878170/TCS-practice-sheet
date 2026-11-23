class A:
  def __init__(self):
    self.a=100;
    self.b=200

  def display(self,a,b):
    print(a)
    print(b)

a=A()
print(a.a)
print(a.b)
a.display(300,400)