#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i > 6:
  print(i)
i += 1

#BREAK statement
#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#CONTINUE Statement
#skips the current iteration when i is equal to 3, and continues the next iteration. Hence, the output has all the values except 3.

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  #ELSE Statement
  #With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


  #FOR LOOP
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["Apple","Banana","Cherry"]
for x in fruits:
  print(x)

#LOOPING THROUGH A STRING
#Even strings are iterable objects, they contain a sequence of characters:

for x in "banana":
  print(x)
# BREAK STATEMENT
#With the break statement we can stop the loop before it has looped through all the items:
Fruits = ["Apple","banana","cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# CONTINUE STATEMENT
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
Fruits = ["Apple","banana","Cherry"]
for x in fruits:
  if x == "banana":
    continue
    print(x)

# THE RANGE FUNCTION
#To loop through a set of code a specified number of times, we can use the range() function,
for x in range(6):
  print(x)
  
# ELSE IN FOR LOOP
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished")

# NESTED LOOP
#The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)






