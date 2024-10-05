#Arithematic Operator
x = 3
y = 3
print(x + y) #Addition
print(x - y) #Subtraction
print(x * y) #Multiply
print(x / y) #Division
print(x % y) #Module
print(x // y) #Exponention
print(x ** y) #Floor Divion

#Assignment Operator
x = 6
print(x)

y = 3
y += 3
print(y)

a = 9
a -= 3
print(a)

b = 3
b *= 2
print(b)

x = 3
x /= 3
print(x)

y = 6
y %= 6
print(y)

a = 6
a //= 6
print(a)

b = 6
b **= 6
print(b)

x = 6
x &= 6
print(x)

y = 6
y |= 6
print(y)

a = 3
a ^= 3
print(a)

b = 3
b >>= 3
print(b)

x = 3
x <<= 3
print(x)

y = 3
print(y := 3)

#Comparision Operator
x = 5
y = 1
print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

#Python Logical Operator

x = 6 #Returns True if both statements are true
print(x > 3 and x < 10)

x = 6 #Returns True if one of the statements is true
print(x > 3 or x < 10)

x = 6 #Reverse the result, returns False if the result is true
print(not(x > 3 and x < 10))

#Python Identity Operator
x = ["apple","banana","orange"]
y = ["apple","banana","orange"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership operator
x = ["apple","banana"]
print("banana" in x) #Returns True if a sequence with the specified value is present in the object

y = ["apple","banana"]
print("orange" not in y) #Returns True if a sequence with the specified value is not present in the object

#Bitwise Operator
print(6 & 3) #Sets each bit to 1 if both bits are 1
print(6 | 3) #Sets each bit to 1 if one of two bits is 1
print(6 ^ 3) #Sets each bit to 1 if only one of two bits is 1
print(~6) #Inverts all the bits
print(6 >> 3) #Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(6 << 3) #Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off