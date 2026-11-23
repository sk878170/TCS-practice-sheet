# filter

a=[x for x in range(11)]

def even(n):
  if n%2==0:
    return True
  else:
    return False

eve=list(filter(even,a))

print(eve)

# map

a=[x for x in range(1,11)]

def divide(n):
  if n%2==0:
    return n//2
  else:
    return n

div=list(map(divide,a))
print(div)



  