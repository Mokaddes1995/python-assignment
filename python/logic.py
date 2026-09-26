# Week 1 — Fundamentals + Thinking Habit

# Day 1 — Input, Output & Variables

# Exercise 1

name = input("Enter Your Name: ")

age = int(input("Enter Your Age: "))

town = input("Enter Your Town Name: ")

print(f"Name: {name}")

print(f"Age: {age}")

print(f"Town Name: {town}")

# Exercise 2

new_age = age + 5

print(f"After 5 Years: {new_age}")

# Exercise 3

length = float(input("Length: "))

width = float(input("Width: "))

area = length * width

print(f"Area = {area:.2f}")

# Exercise 4

celsius = float(input('Enter Your Temp: '))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")


# Day 2 Exercises

# Exercise 1 — Data Types

name = "Rahim"
age = 32
height = 5.6
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# Exercise 2 — Basic Calculator

first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

# Addition

addition = first_number + second_number

# Subtraction

subtraction = first_number - second_number

# Multiplication

multiplication = first_number * second_number

# Division

division = first_number  / second_number

division_2 = first_number  // second_number

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division Float: {division}")
print(f"Division Int: {division_2}")


# Exercise 3 — Remainder

number = int(input("Input Your Number: "))

# Remainder

remainder = number % 2

print(f"Remainder by 2 = {remainder}")

remainder = number % 3

print(f"Remainder by 3 = {remainder}")

remainder = number % 5

print(f"Remainder by 5 = {remainder}")


# Exercise 4 — Square & Cube

num =  int(input("Number: "))

square = num ** 2

cube = num ** 3

print(f"Square: {square}")

print(f"Cube: {cube}")

# Exercise 5 ⭐ — Even / Odd

number = int(input('Number: '))

if number % 2 != 0:

    print("Odd Number")

else: 

    print('Even Number')


# Exercise 6 ⭐⭐ — Shopping Calculation

product_price = int(input("Product Price: "))

discount = int(input("Discount: "))

# Discount Amount

discount_amount = product_price * discount // 100

final_price = product_price - discount_amount

print(f"Discount Amount: {discount_amount}")

print(f"Final Price: {final_price}")


# Day 3 — Conditions

# Practice 1 — if

age = 18

if age >= 18:
    print("Adult")
    

#  Practice 2 — Odd or Even

n = 5

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
    
# Practice 1 — Max Number of 3

a = 10

b = 20

c = 40

if a > b and a > c:
    print("A Greater Than B & C")
elif b > a and b > c:
    print('B Greater Than A & C')
else:
    print("C Greater Than A & B")

