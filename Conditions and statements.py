#An "if statement" is written by using the if keyword.
a = 33
b = 33
if(a > b):
  print("a is greater than b")

#The else keyword catches anything which isn't caught by the preceding conditions.
a = 33
b = 64
if(a > b):
  print("a is greater than b")
else:
  print("a is less than b")

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if(a > b):
  print("a is greater than b")
elif a == b:
  print("a and b are equal")

#NESTED IF
#You can have if statements inside if statements, this is called nested if statements.

x = 41
if(x > 10):
  print("above ten")
  if(x > 20):
    print("and also above 20!")
  else:
      print("but not above 20.")


