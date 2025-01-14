#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "Fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)