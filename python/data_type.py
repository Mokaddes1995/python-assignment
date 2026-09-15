#Data Types

#String Data

x = "Mokaddes"



print(type(x))

#Number

x = 4 #This is integer

print(x)

print(type(x))

y = 4.0 #This is float

print(y)

print(type(y))

#Tuple

x = ("Mokaddes", 4, 3.0)

print(x)

print(type(x))

#List Data

y = ['Mokaddes', 4, 5, 5.0, True, False]

print(y)

print(type(y))

#Boolean Data

x = True
y = False

print(x)
print(y)

print(type(x))
print(type(y))

#Set Data

x = {'Mokaddes', 2, 3, 3, 5}

print(x)
print(type(x))

#Dict Data

my_dict = {"fname" : "Mokaddes", "age" : 30}

print(my_dict)
print(type(my_dict))

#Range Data

x = range(5)

print(x)
print(type(x))

#Specific Data Type

a = ("Apple", "Orange", 3, "Mango", "Banana", 5)
print(a)
print(type(a))

b = 3

c = str(("Apple", "Orange", 3, "Mango", "Banana", 5))
print(c)
print(type(c))

d = list(a)
print(d)
print(type(d))

e = dict(fruits = "Apple", price = 180)
print(e)
print(type(e))

import math

x = 3.4
y = 4.6

print(round(x))

print(math.ceil(x))
print(math.floor(y))
print(math.trunc(x))