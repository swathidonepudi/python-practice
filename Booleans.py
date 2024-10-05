#Booleans represent one of two values: True or False.

#Boolean Values
print(10 > 9) #In programming you often need to know if an expression is True or False.

print(10 == 9) #You can evaluate any expression in Python, and get one of two answers, True or False.

print(10 < 9) #When you compare two values, the expression is evaluated and Python returns the Boolean answer:

#When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33
if(a > b):
  print("a is greater than b")
else:
  print("a is less than b")

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello")) #Evaluate a string and Number
print(bool(15))

x = "Hello"
y = 15
print(bool(x)) #Evaluate two variables:
print(bool(y))

#Most values are True
#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["Momma", "Daddy", "Anaya","Oreo"])

#Some values are False
#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#FUNCTION CAN RETURN A BOOLEAN VALUES

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  #Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))
