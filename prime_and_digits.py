# Devise a program that inputs a 3 digit number n and finds out whether the number is 
# prime or not. Find out its factors. 

n=int(input())

def prime(n):
    count=0
    factors=[]
    if n<=1:
        return False
    for i in range(2,n//2):
        if n%i==0:
            count+=1
            factors.append(i)

    if count==0:
        return True
    return factors

print(prime(n))