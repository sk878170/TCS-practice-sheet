str1="i love cheese and mac"

str2="love"
str3="cheeseand"
str4="m"
str5="z"

try:

  print(str1.find(str2))
  print(str1.find(str3))
  print(str1.find(str5))

except Exception as e:
  print("Error",e)

try:
  print(str1.index(str2))
  print(str1.index(str3))
  print(str1.index(str4))
  print(str1.index(str5))

except Exception as e:
  print("Error",e)
  

try:
  print(str1.rindex(str2))
  print(str1.rindex(str3))
  print(str1.rindex(str4))
  print(str1.rindex(str5))

except Exception as e:
  print("Error",e)

try:
  print(str1.rfind(str2))
  print(str1.rfind(str3))
  print(str1.rfind(str4))
  print(str1.rfind(str5))

except Exception as e:
  print("Error",e)