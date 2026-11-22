# Write a program to reverse a string.

str1="hello"

print(str1[::-1])

rev_str=""

for i in str1:
    rev_str=i+rev_str

print(rev_str)