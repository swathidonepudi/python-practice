#Numeric Types
x = 6 
y = 5.8 
z = 5j
print(type(x))
print(type(y))
print(type(z))

#Type conversion

x = 6
y = 5.8
z = 5j

a = (float(x))
b = (int(y))
c = (complex(z)) #you cannot convert complex into another number type
print(a)
print(b)
print(c)

print(type(x))
print(type(y))
print(type(z))


#Random number
import random
print(random.randrange(1, 10))
