#You can display a string literal with the print() function:
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')

#Quotes inside Quotes
print("it's all right") #You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("she is called 'Swathi'")

#Assign strings to a variable
a = "Hello"  #Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
print(a)

#Multiline Strings
a = """You can assign a multiline string to a variable by using three quotes
these are multiline strings,these multiline strings indicates with three double quotes"""
print(a)

a = '''"""You can assign a multiline string to a variable by using three quotes
these are multiline strings,these multiline strings indicates with three single quotes'''
print(a)

#Strings are Arrays
#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

#looping through a string
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "Swathi": #Loop through the letters in the given word:
  print(x)

#String Length
#To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:
txt = "The best things in life are free!" #Print only if "free" is present:
if "free" in txt:
  print("Yes, 'free' is present.")

  #Check If Not
  #To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!" #Check if "expensive" is NOT present in the following text:
print("expensive" not in txt)

#Use it in an if statement:
txt = "The best things in life are free!" #print only if "expensive" is NOT present:
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")




