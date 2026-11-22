def fibonacci(n):
  if n<=1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input())
fib=[]
for i in range(n):
  print(fibonacci(i))

for i in range(n):
  fib.append(fibonacci(i))
print(fib)