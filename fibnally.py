def func():
  try:
    a=0
    b=100
    c=50
    print(a/b)
    print(b/c)
    print(c/a)
  except :
    return 0
  print("This is print block")

def func2():
  try:
    a=0
    b=100
    c=50
    print(a/b)
    print(b/c)
    print(c/a)
  except :
    return 0
  finally:
    print("This is finally block")

func()
func2()
