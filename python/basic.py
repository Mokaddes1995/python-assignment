#Print First Code

print("Hello World!")

#Python Comments

#This is a comment

"""This is a multi-line comment
this is a multi-line comment
this is a multi-line comment"""

#Python Variables

x = "This is a variable"

y = 5 #This is also variable

print(x)
print(y)

#Python Casting

x = int(3)  # x is now 3
y = str(3)  # y is now "3"
z = float(3)# z is now 3.0

print(x)
print(y)
print(z)

#Get Data Types

print(type(x))

#Variable Name

myvar = 'This is a string'

_my_var = "This is a string"

my_var = 5

MYVAR = 7

myVar = 9

myvar2 = "Mokaddes Hossain"

#Camel Case

myVariableName = "John"

#Snake Case

my_variable_name = 7

#Pascal Case

MyVariableName =  "John"

#Assign Multiple value to Multiple Variables

x,y,z = 'Orange', 'Banana', "Mango"

print(x) #Orange
print(y) #Banana
print(z) #Mango

#Assign One Value Multiple Variables

x = y = z = "Orange"

print(x) #Orange
print(y) #Orange
print(z) #Orange  

#Unpack Collection

fruits = ("Apple","Orange","Mango")

x,y,z = fruits

print(x) #Apple
print(y) #Orange
print(z) #Mango

#Personal Profile Builder

print("===========Personal Profile Builder===========")
print(" ")
print(' ')

#Create Variables

fname = "MD MOKADDES"
lname = "HOSSAIN"
age = 30
height = 170.0
weight = 69
email = 'monarulislam443@gmail.com'
phone ="01740097310"

print("")
print(' ')

#Calculate BMI

print("=========Calculate BMI=========")

print("")

print("")

#Convert Height cm to Meter

convert_height = height/100

#Calculate BMI

bmi = 69/(convert_height**2)

print(f"First name: {fname}")
print(f"Last name: {lname}")
print(f"Age: {age}")
print(f"Height in cm: {height}")
print(f"Weight in Kg: {weight}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Calculate BMI: {bmi:.2f}")

#Birth Year

print("========Birth Year=======")
print()

birth_year = 2026- age

print(f"Birth Year: {birth_year}")

#Task 2: Multiple Assignment Challenge

#Create Variables

a,b,c = 5,10,15

print(f"Initial:a={a}, b={b}, c={c}")

#Swap Variables

a,b,c = b,c,a

print(f"After Assign: a ={a}, b ={b}, c = {c}")

#Create Three value

x, y, z = 1, 2, 3
print(f"Initial:x={x}, y={y}, z={z}")

x,y,z  = 10,20,30
print(f"After New Assign: x = {x}, y = {y}, z = {z}")

#One line Assign

p = q = r = 0
print(p,q,r)

#Delete variable

x = 5
print(x)

del x

print(x) #Show Error because x are delete
