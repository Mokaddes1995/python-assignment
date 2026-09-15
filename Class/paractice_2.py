# LEVEL 1: Basic Syntax (টাস্ক ১-৮)

# Task 1: Hello World

# Print "Hello, World!" using print statement

print("Hello, World!")

# Task 2: Variables

# Create three variables: name (string), age (int), height (float)
# Print them using f-string


name = "Mokaddesh Hossain"

age = 32

height = 5.6

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")


# Task 3: Multiple Assignment

# Assign values to multiple variables in one line
# a = 10, b = 20, c = 30
# Print sum of all three

a, b, c = 10, 20, 30

print(a + b + c)


# Task 4: Type Checking

# Create variables of different types (int, float, str, bool)
# Print their types using type()


integer = 10

flo = 20.0

string = "Mokaddes Hossain"

boolean = True

print(type(integer))

print(type(flo))

print(type(string))

print(type(boolean))


# Task 5: Input and Print

# Take user's name and age as input

name = input("Name: ")
age = int(input("Age: "))

# Print "Hello [name], you are [age] years old"

print(f"Hello {name}, you are {age} years old")


# Task 6: Comments

# Write a program with:

# - Single line comment

# This is Single line Comment

a = "Python is fun!"

# - Multi-line comment

'''
This is 
Multi 
Line Comment
'''

# - Code that prints "Python is fun!"

print(a)


# Task 7: Variable Swapping

# Swap two variables without using a third variable
# a = 5, b = 10 → a = 10, b = 5

a = 5

b = 10

a, b = b, a

print(a, b)


# Task 8: String Concatenation

# Concatenate three strings using + operator
# word1 = "Python", word2 = "is", word3 = "awesome"
# Print the result

word1 = "Python", 
word2 = "is", 
word3 = "awesome"

result = word1 + " " + word2 + ' ' + word3

print(result)


# LEVEL 2: Data Types (টাস্ক ৯-১২)

# Task 9: Integer Operations

# Take two integers as input

num_1 = int(input("Num_1: "))

num_2 = int(input('Num_2: '))

# Print: sum, difference, product, division, modulus

sum = num_1 + num_2

print(f"Sum: {sum}")

difference = num_1 - num_2

print(f"Difference: {difference}")

product = num_1 * num_2

print(f"Product: {product}")

division = num_1 / num_2

print(f"Division: {division}")

modulus = num_1 % num_2

print(f"Modulus:{modulus}")


# Task 10: Float Operations

# Take two float numbers as input

num_1 = float(input("Num_1: "))

num_2 = float(input("Num_2: "))

# Print sum rounded to 2 decimal places

sum = num_1 + num_2

print("Rounded Sum:", round(sum))

print(f"2 Decimal Sum: {sum:.2f}")


# Task 11: Boolean Logic

# Take two numbers as input

num_1 = int(input("Num_1: "))

num_2 = int(input("Num_2: "))

# Print True if first > second, otherwise False

if num_1 > num_2:
    print(True)
else:
    print(False)
    
# Task 12: Type Conversion

# Convert string "123" to integer, float, and boolean

# Print all results with their types

string = '123'

print(type(int(string)))

print(type(float(string)))

print(type(bool(string)))


# LEVEL 3: String Operations (টাস্ক ১৩-১৮)

# Task 13: String Length

# Take a string input and print its length

string = input("Enter String: ")

print(len(string))


# Task 14: Upper and Lower

# Take a string input

string = input("Enter String: ")

# Print it in uppercase and lowercase

upper_case = string.upper()

print(f"Upper Case String: {upper_case}")

lower_case = string.lower()

print(f"Lowe Case String: {lower_case}")


# Task 15: String Slicing

# Take a string input

string = input("Enter String: ")

# Print: first 3 chars, last 3 chars, reverse of string

print(f"Frist 3 Char: {string[:3]}")

print(f"Last 3 Char: {string[-3:]}")

print(f"Reverse String: {string[::-1]}")


# Task 16: Count Characters

# Take a string and a character as input

string = input("Enter String: ")

char = input("Enter Char: ")

# Count how many times the character appears

print(f"{string} appears {char} is {string.count(char)} times")


# Task 17: String Replacement

# Take a sentence and replace all spaces with '_'

string = input("Enter String: ")

print(string.replace(' ', '_'))


# Task 18: Check Substring

# Take a string and check if it contains "Python"

string = input("Enter String: ")

# Print True or False

print("Python" in string)


# LEVEL 4: List Operations (টাস্ক ১৯-২৫)

# Task 19: Create List

# Create a list of 5 favorite fruits

fruits = ['apple', 'banana', 'mango', 'kiwi', 'orange']

# Print the list and its length

print(fruits)

print(len(fruits))


# Task 20: Access List Elements

# From the fruits list, print:

fruits = ['apple', 'banana', 'mango', 'kiwi', 'orange']

# - First element

print(fruits[0])

# - Last element

print(fruits[-1])

# - Middle element (index 2)

print(fruits[2])


# Task 21: List Manipulation

# Start with a list [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4, 5]

# Add 6 at the end

my_list.append(6)

# Insert 0 at the beginning

my_list.insert(0, 0)

# Remove the last element

my_list.pop()

# Print the final list

print(my_list)


# Task 22: List Slicing

# Create a list of numbers 1-10

my_list = [1,2,3,4,5,6,7,8,9,10]

# Print: first 5, last 5, every 2nd element

print(f"First 5 : {my_list[:5]}")

print(f"Last 5 : {my_list[-5:]}")

print(f"First 2nd Element: {my_list[1]} ")

print(f"Last 2nd Element: {my_list[::2]}")


# Task 23: List Comprehension

# Use list comprehension to create:

# 1. Squares of numbers 1-10

squares = [num ** 2 for num in range(1, 11)]

# 2. Even numbers from 1-20

even = [num for num in range(1, 21) if num % 2 == 0]

# Print both lists

print(squares)

print(even)


# Task 24: List Methods

# Take a list of numbers [5, 2, 8, 2, 9, 2, 7]

new_list = [5, 2, 8, 2, 9, 2, 7]

# Find: maximum, minimum, sum, count of 2

# max number

max_num = max(new_list)

print(max_num)

#Alternative Way

max_num = new_list[0]

for i in new_list:
    
    if i >= max_num:
        max_num = i
        
print(max_num)


# minimum number

min_num = min(new_list)

print(min_num)

# Alternative Way

min_num = new_list[0]

for num in new_list:
    
    if num <= min_num:
        
        min_num = num
        

print(min_num)

# sum

total = sum(new_list)

print(total)

# Alternative Way

total = 0

for num in new_list:
    
    total += num

print(total)

# count of 2

print(new_list.count(2))

# Alternative Way

total = 0

for i in new_list:
    
    if i == 2:
        total += 1
        
print(total)
    
# Sort the list (ascending and descending)

# ascending

new_list = [5, 2, 8, 2, 9, 2, 7]

new_list.sort()

print(new_list)

# descending

new_list.sort(reverse=True)

print(new_list)


# Task 25: Nested List

# Create a nested list (matrix) 3x3

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
# Print the matrix row by row

print()

print("Matrix Row:")

print()

for i in matrix:
    print(i)

print()

# Print the diagonal elements

print("Diagonal: ")

print()

for i in range(len(matrix)):
    print(matrix[i][i])
    

# LEVEL 5: Tuple & Set (টাস্ক ২৬-৩১)

# Task 26: Create Tuple

# Create a tuple of 5 colors

my_tuple = ('Red', 'White', 'Green', 'Blue', 'Pink')

# Print the tuple and its length

print(my_tuple)

print(len(my_tuple))


# Task 27: Tuple Operations

# Create two tuples (1,2,3) and (4,5,6)

tuple_1 = (1,2,3)

tuple_2 = (4,5,6)

# Concatenate them

new_tuple = tuple_1 + tuple_2

print(new_tuple)

# Repeat the first tuple 3 times

print(tuple_1 * 3)


# Task 28: Tuple Unpacking

# Create a tuple (name, age, city) = ("Alice", 25, "NYC")

person = ("Alice", 25, "NYC")

# Unpack and print each value

name, age, city = person 

print(name)
print(age)
print(city)


# Task 29: Create Set

# Create a set of 5 numbers with some duplicates

myset = {1,2,2,3,4,5,5,6,7,7,8,9,9}

# Print the set (duplicates removed)

print(myset)

# Add a new number

myset.add(10)

print(myset)

# Remove a number

myset.discard(10)

print(myset)



# Task 30: Set Operations

# Given two sets A={1,2,3,4} and B={3,4,5,6}

A={1,2,3,4}
B={3,4,5,6}

# Find: union, intersection, difference (A-B), symmetric difference

# union

C = A | B

C = C.union(B)

print(C)

# intersection

D = A & B

D = A.intersection(B)

print(D) # 3,4

# difference

E = A - B

print(E) # 1,2

# symmetric difference

F = A.symmetric_difference(B)

print(F)


# Task 31: Set vs List

# Convert a list with duplicates [1,2,2,3,3,3,4] to set

my_list = [1,2,2,3,3,3,4]

my_set = set(my_list)

print(my_set)

# Then convert back to list (duplicates removed)

my_list_2 = list(my_set)

print(my_list)

# Print both

print(my_set)

print(my_list_2)


# LEVEL 6: Dictionary (টাস্ক ৩২-৩৭)

# Create a dictionary with 3 key-value pairs

person = {
    'name': 'Mokaddes Hossain',
    'age' : 32,
    'city': 'Dhaka'
}

# Keys: name, age, city
# Print the dictionary

print(person)


# Task 33: Access Dictionary

person = {
    'name': 'Mokaddes Hossain',
    'age' : 32,
    'city': 'Dhaka'
}

# From the person dictionary, print:

# - Name using key

print(person['name'])

# - Age using get() method

print(person.get('age'))

# - City with default "Unknown" if not found

print(person.get('city','Unknown'))


# Task 34: Dictionary Operations

person = {
    'name': 'Mokaddes Hossain',
    'age' : 32,
    'city': 'Dhaka'
}

# Add a new key "country" with value "USA"

person.update({'country': 'USA'})

person['country'] = 'USA'

# Update age to 26

person.update({'age': 26})

person['age'] = 26

# Remove city

person.pop('city')

# Print the final dictionary

print(person)


# Task 35: Dictionary Loop

# Create a dictionary of 3 students with their scores

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Loop through and print each student and their score

for key, value in scores.items():
    print(f"Name: {key}")
    print(f"Scores: {value}")


# Task 36: Dictionary Comprehension

# Create a dictionary of squares for numbers 1-5
# Using dictionary comprehension

my_dict = {k : k**2 for k in range(1,6) }

print(my_dict)


# Task 37: Dictionary Methods

# Given dictionary {"a": 1, "b": 2, "c": 3}

my_dict = {"a": 1, "b": 2, "c": 3}

# Print: all keys, all values, all items

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

# Clear the dictionary

my_dict.clear()

print(my_dict)


# LEVEL 7: Functions (টাস্ক ৩৮-৪৪)

# Task 38: Simple Function

# Create a function that prints "Hello, World!"

def simple_func():
    print('Hello, World!')

# Call the function

simple_func()


# Task 39: Function with Parameters

# Create a function that takes two numbers and returns their sum

def sum_func(a, b):
    
    return a + b

# Call the function with 5 and 3

print(sum_func(5, 3))


# Task 40: Function with Default Parameter

# Create a function greet(name, greeting="Hello")

def greet(name, greeting = 'Hello'):
    
    print(f"{greeting}, {name}")

# Call with name only and with both parameters

greet('Mokaddes')

greet('Mokaddes', 'Hi')


# Task 41: Function with *args

# Create a function that takes any number of numbers
# Returns their sum

def add(*num):
    return sum(num)

print(add(5,6,7,8))


# Task 42: Function with **kwargs

# Create a function that prints keyword arguments

def greet(**kwargs):
    
    print(f"My name is {kwargs['name']}, Age {kwargs['age']} and City {kwargs['city']}")

# Call with name, age, city

greet(name = 'Mokaddes Hossain', age = 32, city = "Dhaka")


# Task 43: Return Multiple Values

# Create a function that takes a list of numbers

def list_func(num):
    
    total = sum(num)
        
    average = total/len(num)
    
    max_num =  max(num)
    
    min_num = min(num)
    
    return f"Total: {total}", f"Average: {average}", f"Max Number: {max_num}", f"Minimum Number: {min_num}"


# Returns: sum, average, max, min

my_list = [1,2,3,4,5,6,7,8]

# tuple unpacking

total, average, max_num, min_num = (list_func(my_list))

print(total)

print(average)

print(max_num)

print(min_num)


# Task 44: Lambda Function

# Create lambda functions for:
# 1. Square of a number

square = lambda x : x **  2

print(square(5))

# 2. Check if a number is even

is_even = lambda x : x % 2 == 0

print(is_even(6))

# Use them with map() and filter()

# map()

numbers = [1,2,3,4,5,6]

new_numbers = list(map(lambda x : x**2, numbers))

print(new_numbers)


# filter()

filter_numb = list(filter(lambda x : x % 2 != 0, numbers))

print(filter_numb)


# LEVEL 8: Range & Loops (টাস্ক ৪৫-৫০)

# Task 45: Basic Range

# Print numbers from 1 to 10 using range

for num in range(1,11):
    print(num)


# Task 46: Range with Step

# Print even numbers from 0 to 20 using range with step

for num in range(0, 21, 2):
    print(num)


# Task 47: Nested Loops

for i in range(1, 6):
    
    print('*' * 30 )
    print(f"Multiplication of {i}")
    print('*' * 30 )
    
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
        
        
# Task 48: While Loop

# Print numbers from 10 to 1 using while loop

i = 10

while i >= 1:
    
    print(i)
    
    i -= 1
    

# Task 49: Break and Continue

# Print numbers 1-20
# Break when number is 15
# Skip even numbers using continue

i = 0

while i <= 20:
    
    i += 1
    
    if i == 16:
        break
    elif i % 2 == 0:
        continue
    else:
        print(i)
        

# Task 50: Enumerate

fruits = ['apple', 'orange', 'kiwi', 'mango', 'cherry']

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

