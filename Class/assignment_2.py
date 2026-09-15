# Part A — Syntax & Variables

# 1. What is Python? List three features of Python.

'''
Ans:Python is a High Level Programming Language. It was created by Guido van Rossum, and released in 1991.

List of three features of Python:

a. Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc)
b. Python has a simple syntax similar to the English language.
c. Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
'''

# 2.  Explain the following with examples: 
#  Variable 
#  Assignment statement 
#  Comment 
#  Indentation

'''
Ans:

Variable: Variables are container of storing data values.

Assignment statement: Assignment statement use to create variable for assign value. In python (=) is assignment operator.

Comment: In python Comment are use for not execute code. (#) for use single comment and (''' ''') use for multiline comment.

Indentation: Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. use space or tab in same amount in same block of code.
 
'''

# 3.  What will be the output of the following code? 

x = 10 

y = 5 

x = x + y # override value x = 15  

y = x - y # override value y = 10

print(x) # output: 15

print(y) # output: 10

# 4.  Write a Python program that stores your name, age, department, and CGPA in variables and displays them in a formatted sentence.

# Stores Data

name = "Md Mokaddes Hossain"
age = 25
department = "CSE"
cgpa = 3.50

# Display as formatted Sentence

print(f"My Name is {name}, Age {age}, Department {department} and CGPA {cgpa}.")

# 5.  Write a program that takes the length and width of a rectangle as input and calculates:

# Take Input

length = float(input("Enter your Length: "))

width = float(input("Enter your Width: "))
 
# Area 

area = length * width

# Perimeter

perimeter = 2 * (length + width) 

print(f"Area Of Rectangle is {area:.2f}.")

print(f"Perimeter of Rectangle is {perimeter:.2f}.")


# 6.  Identify and correct the errors in the following code: 

name = "Rahim" 
age = 20 
 
print("My name is ", name) # Separate With Coma (',') Or Concatenating ('+')
print("My name is " + name)
print("I am", age, "years old") # Separate With Coma (',') Or use formatted string (f"")
print(f"I am {age} years old")


# Part B — Data Types

# 7.  Explain the following Python data types with one example each: 

#  int 
#  float 
#  str 
#  bool 
#  list 
#  tuple 
#  dict 
#  set

"""
Answer:

int: In Python int means Integer Number.

x = 5

float: In Python float means Decimal Number.

x = 5.0

str : In Python str means String Data. Which mark as Single Quotation mark (' ') or Double Quotation Marks (" ").

x = "Mokaddes"

bool: In Python bool means Boolean Data which returns True or False. When Write first letter are Capital letter.

x = True
x = False

list: In Python Lists are used to store multiple items in a single variable. its create using square brackets.

x = ['apple', True, 1, 2, "Orange"]

tuple: Tuples are used to store multiple items in a single variable.A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

x = ("apple", "Orange" )

dict: Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.Dictionaries are written with curly brackets, and have keys and values.

x = {"name":"Mokaddes", "age": 31}

set: Sets are used to store multiple items in a single variable.A set is a collection which is unordered, unchangeable*, and unindexed.Set items are unchangeable, but you can remove items and add new items.Sets are written with curly brackets.

x = {1,2,3,4,5}  # Set do not store duplicate data.

"""

# 8.  Write a program that takes two numbers from the user and displays:

# Take Input

num_1 = int(input("Number 1: ")) 
num_2 = int(input("Number 2: "))

#  Sum 

sum = num_1 + num_2

print(f"Sum: {sum}")

#  Difference 

difference = num_1 - num_2

print(f"Difference: {difference}")

#  Product 

product = num_1 * num_2

print(f"Product: {product}")

#  Division

if num_2 == 0:
    print("Can not division by 0")
else:
    division = num_1 / num_2
    print(f"Division: {division:.2f}")

#  Floor division 

if num_2 == 0:
    print("Can not division by 0")
else:
    division = num_1 // num_2
    print(f"Floor Division: {division}")

#  Remainder

if num_2 == 0:
    print("Can not division by 0")
else:
    remainder = num_1 % num_2
    print(f"Remainder: {remainder}")


# 9.  Write a program that converts a temperature from Celsius to Fahrenheit. Formula: Fahrenheit = (Celsius × 9/5) + 32

# Take Temperature

celsius = float(input("Enter Temperature (Celsius): ")) 

# Converted Celsius to Fahrenheit

fahrenheit = (celsius  * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

# 10. Write a program that accepts a student's name and marks in three subjects and calculates the student's total and average marks.

# Take Input by user

student_name = input("Enter Student Name: ")


# Take Number for 3 Subject

mark = []

for i in range(1, 4):
    get_marks = int(input(f"Enter your Marks:{i} " ))
    mark.append(get_marks)


# Create Students in Dictionary

student = {
    "name": student_name,
    "marks": mark
}

# Total Marks by use for loop

total_marks = 0
        
for j in student["marks"]:
        
    total_marks += j

# Calculate Average Mark

average = total_marks/(len(student["marks"]))

# Display Information

print(f"Student Name: {student['name']}")
    
print(f"Total Marks: {total_marks}")

print(f"Average Marks: {average:.2f}")


# 11. Create a list containing five student names. Write Python code to:

# Create a List for five Students Name

student_list = ['Mokaddes', 'Hakim', 'Mahir', 'Raiyan', 'Alim']

# Add a new student

student_list.append('Arif')

# Remove a student 

student_list.remove('Alim')

#  Sort the list 

student_list.sort()

#  Display the number of students

print(len(student_list))


# Part C — Control Flow

# 12. Write a program that takes an integer from the user and determines whether it is:

# Take Input By User

number = int(input("Enter your Integer Number: ")) 

#  Positive

if number > 0:
    
    print(f"{number} is Positive Number")
 
#  Negative 
 
elif number < 0:
    
    print(f"{number} is Negative Number")
        
#  Zero

else:
    print(f"Zero")


# 13. Write a program that takes a student's marks and displays the grade according to the following:

# Take a Marks from User

marks = int(input("Enter your Marks: "))

# Validation of Marks

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
 
# Marks: 80–100    Grade: A+

elif marks >= 80:
    print(f"Marks: {marks}, Grade: 'A+'.")
   
# Marks: 70–79     Grade: A 

elif marks >= 70:
    print(f"Marks: {marks}, Grade: 'A'.")
    
# Marks: 60–69     Grade: B

elif marks >= 60:
    print(f"Marks: {marks}, Grade: 'B'.") 

# Marks: 50–59     Grade: C

elif marks >= 50:
    print(f"Marks: {marks}, Grade: 'C'.") 

# Marks: 40–49     Grade: D

elif marks >= 40:
    print(f"Marks: {marks}, Grade: 'D'.")

# Marks: Below 40  Grade: F

else:
    print(f"Marks: {marks}, Grade: 'F'.")


# 14. Write a program to determine whether a given year is a leap year.

# Take Inputs from User

year = int(input('Enter Year: '))

# Leap Year

if year % 4 == 0 and year % 100 != 0:
    
    print(f"{year} is Leap Year.")
    
elif year % 400 == 0:
    
    print(f"{year} is Leap Year.")
    
else:
    print(f"{year} is not Leap Year.")


# 15. Write a program that takes a number and determines whether it is even or odd.

# Take Input from Users

numbers = int(input("Enter Numbers: "))
    
# Checked Even Or Odd Number
    
if numbers % 2 == 0:
        
    print(f"{numbers} is Evevn Number")
        
else:
        
    print(f"{numbers} is Odd Number")


# 16. Using a for loop, print the multiplication table of a number entered by the user

# Take Input By Users

multi_num = int(input("Enter your Desire Number: "))

# For Space

print()

# Multiplication

for i in range(1, 11):
    
    print(f"{multi_num} x {i} = {multi_num * i}")
    

# 17. Write a program to calculate the sum of numbers from 1 to 100 using a loop.

# Sum of Numbers from 1 to 100 by Using for loop

total = 0

for i in range(1, 100 + 1):
    
    total += i

print(total)


# 18. Write a program that prints all the even numbers between 1 and 50.

# Print all even numbers between 1 and 50 by using for loop

print("even numbers between 1 and 50")

print("-" * 20)

for i in range(1, 50 + 1):
    
    if i % 2 == 0:
        print(i)


# 19. Write a program that asks the user to enter a password repeatedly until the correct password is entered.

# Use While Loop when while loop condition True the loop are continue

while True:
    
    # Take Input from User
    
    password = input('Enter your PassWord: ').lower() # Use lower method for case-insensitive
    
    if password ==  'mokaddes12345':
        
        print("Correct Password...")
        
        print('Thank You')
        
        break # When Password Match Brake the Loop
    else:
        
        # Continue Print this block when password not match
        
        print("Incorrect Password.")
        
        print("Try Again")

# 20. Write a program that calculates the factorial of a number using a while loop.

# Take Input from User

num = int(input("Enter your Number: "))

i = 1

factorial = 1

#Use While Loop

while i <= num:
    
    factorial *= i
    
    i += 1
    
print(f"Factorial of {num} : {factorial}")


# Part D — Functions


# 21. What is a function in Python? Explain the difference between: 

"""
Ans: Function: A function is a block of code which only runs when it is called. A function can return data as a result. A function helps avoiding code repetition.

Function definition: In Python, a function is defined using the def keyword, followed by a function name and parentheses.

def area(length, width):

Function call: To call a function, write its name followed by parentheses.

area(32, 50)

Parameter: A parameter is the variable listed inside the parentheses in the function definition.

def area(length, width):

Argument: An argument is the actual value that is sent to the function when it is called.

area(32, 50)

Return value: Functions can send data back to the code that called them using the return statement.

def area(length, width):
    return length * width

"""

# 22. Write a function called calculate_area() that accepts the radius of a circle and returns its area.

# Define Function Calculate Area with def statement

def calculate_area(r):
    
    pi = 3.141592653589793
    
    return pi * (r**2)

# Take Input from user

radius = int(input("Enter Radius of Circle: "))

# Call Function With Variable

area = calculate_area(radius)

print(f" Area of Circle:{area:.6f}")


# 23. Write a function called is_even() that accepts a number and returns True if the number is even and False otherwise.

# Define Function is_even() with def statement

def is_even(num):
    
    if num % 2 == 0:
        return True
    else:
        return False
    
number = int(input('Enter Number: '))

even_number = is_even(number)

print(even_number)


# 24. Write a function called find_max() that accepts three numbers and returns the largest number.

# Define Function find_max() with def statement

def find_max(a, b, c):   
    
    # Condition
    
    if a >= b and a >= c:
        
        return a
    
    elif b >= a and b >= c:
        
        return b
    
    else:
        
        return c

# Take Input

num_1 = int(input("Number 1: "))

num_2 = int(input("Number 2: "))

num_3 = int(input("Number 3: "))

# Call Function With Variable

max_num = find_max(num_1, num_2, num_3)

print(f"Max Number is {max_num}")


# 25. Write a function called calculate_grade() that accepts a student's marks and returns the appropriate grade.

# Define Function calculate_grade() with def statement

def calculate_grade(marks):

    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter marks between 0 and 100."
    
    # Marks: 80–100    Grade: A+

    elif marks >= 80:
        return f"Marks: {marks}, Grade: 'A+'."
    
    # Marks: 70–79     Grade: A 

    elif marks >= 70:
        return f"Marks: {marks}, Grade: 'A'."
        
    # Marks: 60–69     Grade: B

    elif marks >= 60:
        return f"Marks: {marks}, Grade: 'B'."

    # Marks: 50–59     Grade: C

    elif marks >= 50:
        return f"Marks: {marks}, Grade: 'C'."

    # Marks: 40–49     Grade: D

    elif marks >= 40:
        return f"Marks: {marks}, Grade: 'D'."

    # Marks: Below 40  Grade: F

    else:
        return f"Marks: {marks}, Grade: 'F'."


# Take Input from Users

mark = int(input("Enter Marks: "))

# Call Function with Variable

grade = calculate_grade(mark)

print(grade)


# 26. Write a function called factorial() that accepts an integer and returns its factorial

# Define Function factorial() with def statement

def factorial(num):
    
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i
    
    return factorial

# Take Input from User

fact_num = int(input("Enter Number"))

# Call Function with Variable

fact = factorial(fact_num)

print(f"Factorial {fact_num} is {fact}")


# 27. Write a function called count_vowels() that accepts a string and returns the number of vowels in the string. 

# Define Function count_vowels() with def statement

def count_vowels(word):
    
    vowel = 'aeiouAEIOU'
    
    count = 0
    
    for i in word:
        if i in vowel:
            count += 1
            
    return count


# Take Input

txt = input("Enter String: ")

# Call Function with Variable

vowel_no = count_vowels(txt)

print(vowel_no)