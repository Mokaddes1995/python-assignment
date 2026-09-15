# # Task 1: Hello World

# # Write a function that prints "Hello, World!"

# def hello():
    
#     print("Hello, World!")
    
# # Call Function

# hello()

# # Test: hello()
# # Expected: Hello, World!

# # Task 2: Simple Welcome

# # Write a function that prints "Welcome to Python!"

# def welcome():
    
#     print("Welcome to Python!")

# # Test: welcome()

# welcome()

# # Task 3: Print Star

# # Write a function that prints 5 stars: "*****"

# def print_stars():
    
#     print("*" * 5)

# # Test: print_stars()

# print_stars()

# # Task 4: Greet User

# # Write a function that takes a name and prints "Hello, {name}!"

# def greet(name):
    
#     print(f"Hello, {name}")
    
    
# # Test: greet("Alice") → Hello, Alice!

# greet("Alice")

# #  Task 5: Add Two Numbers

# # Write a function that takes two numbers and returns their sum

# def add(a, b):
    
#     print(a + b)
    
# # Test: add(5, 3) → 8

# add(5,3)

# # Task 6: Multiply Two Numbers

# # Write a function that takes two numbers and returns their product

# def multiply(a, b):
        
#     return a * b

# # Test: multiply(4, 5) → 20

# print(multiply(4, 5))

# # Task 7: Calculate Age

# # Write a function that takes birth year and returns age (assume current year 2024)

# def calculate_age(birth_year):
        
#     return 2024 - birth_year

# # Test: calculate_age(2000) → 24

# print(calculate_age(2000))

# # Task 8: Square a Number

# # Write a function that takes a number and returns its square

# def square(num):
    
#     return num ** 2
    
# # Test: square(5) → 25

# print(square(5))

# # Task 9: Cube a Number

# # Write a function that takes a number and returns its cube

# def cube(num):
    
#     return num ** 3
    
# # Test: cube(3) → 27

# print(cube(3))

# # Task 10: Even or Odd

# # Write a function that checks if a number is even or odd
# # Returns "Even" or "Odd"

# def even_odd(num):
    
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
        

# # Test: even_odd(4) → "Even", even_odd(7) → "Odd"

# print(even_odd(4))
# print(even_odd(7))

# # Task 11: Calculate BMI

# # Write a function that takes weight (kg) and height (m) and returns BMI
# # BMI = weight / (height * height)

# def calculate_bmi(weight, height):
    
#     bmi = weight / (height ** 2)
    
#     return f"{bmi:.2f}"

# # Test: calculate_bmi(70, 1.75) → 22.86

# print(calculate_bmi(70, 1.75))

# # Task 12: Rectangle Area

# # Write a function that takes length and width and returns area of rectangle

# def rectangle_area(length, width):
    
#     return length * width

# # Test: rectangle_area(5, 3) → 15

# print(rectangle_area(5, 3))

# # Task 13: Circle Area

# # Write a function that takes radius and returns area of circle (πr²)
# # Use 3.1416 for π
# def circle_area(radius):
    
#     circle = 3.1416 * (radius ** 2)
    
#     return round(circle, 2)

# # Test: circle_area(7) → 153.94

# print(circle_area(7))

# # Task 14: Triangle Area

# # Write a function that takes base and height and returns area of triangle
# # Area = 0.5 * base * height

# def triangle_area(base, height):
        
#     return 0.5 * base * height

# # Test: triangle_area(10, 5) → 25

# print(triangle_area(10, 5))

# # Task 15: Temperature Converter

# # Write a function that converts Celsius to Fahrenheit
# # Fahrenheit = (Celsius × 9/5) + 32

# def celsius_to_fahrenheit(celsius):
    
#     Fahrenheit = (celsius * 9/5) + 32
    
#     return f"{Fahrenheit:.2f}"
    
# # Test: celsius_to_fahrenheit(0) → 32

# print(celsius_to_fahrenheit(0))

# # Task 16: Currency Converter

# # Write a function that converts USD to BDT (1 USD = 110 BDT)

# def usd_to_bdt(usd):
#     rate = 110
    
#     return usd * rate

# # Test: usd_to_bdt(10) → 1100

# print(usd_to_bdt(10))

# # Task 17: Largest of Three

# # Write a function that takes three numbers and returns the largest

# def largest(a, b, c):
    
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# # Test: largest(5, 9, 3) → 9

# print(largest(5, 9, 3))

# # Task 18: Power Function

# # Write a function that takes a number and an optional power (default 2)
# def power(num, exp=2):

#     return num ** exp

# # Test: power(3) → 9, power(3, 3) → 27

# print(power(3))
# print(power(3,3))

# # Task 19: Greeting with Default

# # Write a function that greets with default name "Guest"

# def greet_default(name="Guest"):
    
#     print(f"Hello, {name}!")

# # Test: greet_default() → Hello, Guest!
# #       greet_default("Alice") → Hello, Alice!

# greet_default()
# greet_default("Alice")

# # Task 20: Discount Calculator

# # Write a function that calculates discount (default discount 10%)
# def calculate_discount(price, discount=10):
    
#     percentage = (discount /100) * 100
    
#     return f"{(price - percentage):.2f}"

# # Test: calculate_discount(100) → 90
# #       calculate_discount(100, 20) → 80

# print(calculate_discount(100))
# print(calculate_discount(100, 20))

# # Task 21: Sum of List

# # Write a function that takes a list of numbers and returns their sum
# def sum_list(numbers):
#     sum = 0
#     for i in numbers:
#         sum  += i
#     return sum

# # Test: sum_list([1, 2, 3, 4, 5]) → 15

# print(sum_list([1, 2, 3, 4, 5]))

# # Task 22: Average of List

# # Write a function that takes a list of numbers and returns their average

# def average_list(numbers):
    
#     total = 0
#     length = 0
    
#     for i, num in enumerate(numbers):
#         total += num
        
#         length += 1
    
#     aver = total / length
    
#     return aver

# # Test: average_list([10, 20, 30]) → 20

# print(average_list([10, 20, 30]))

# # Task 23: Find Maximum

# # Write a function that takes a list of numbers and returns the maximum
# def find_max(numbers):
    
#     max_numbers = max(numbers)
    
#     return max_numbers

# # Test: find_max([3, 7, 2, 9, 4]) → 9

# print(find_max([3, 7, 2, 9, 4]))

# # Alternative Number
# def find_max(numbers):
    
#     max_num = numbers[0]

#     for num in numbers:
    
#         if num > max_num:
#             max_num = num
        
#     return max_num

# print(find_max([3, 7, 2, 9, 4]))

# # Task 24: Find Minimum

# # Write a function that takes a list of numbers and returns the minimum
# def find_min(numbers):
    
#     min_number = min(numbers)
    
#     return min_number

# # Test: find_min([3, 7, 2, 9, 4]) → 2

# print(find_min([3, 7, 2, 9, 4]))


# # Alternative

# def find_min(numbers):
    
#     min_number = numbers[0]
    
#     for num in numbers:
#         if num < min_number:
#             min_number = num
    
#     return min_number

# # Test: find_min([3, 7, 2, 9, 4]) → 2

# print(find_min([3, 7, 2, 9, 4]))


# # Task 25: Reverse List

# # Write a function that takes a list and returns it reversed
# def reverse_list(items):
    
#     reverse_item = items[::-1]
    
#     return reverse_item

# # Test: reverse_list([1, 2, 3, 4]) → [4, 3, 2, 1]

# print(reverse_list([1, 2, 3, 4]))

# # Alternative

# def reverse_list(items):
    
#     reverse_item =[]
    
#     for i in range(len(items)):
#         i += 1
#         reverse_item.append(items[-i])        
        
#     print(reverse_item)

# reverse_list([1, 2, 3, 4])

# # Task 26: Remove Duplicates

# # Write a function that removes duplicates from a list

# def remove_duplicates(items):
    
#     new_list = [set(items)]
    
#     return new_list

# # Test: remove_duplicates([1, 2, 2, 3, 3, 3, 4]) → [1, 2, 3, 4]

# print(remove_duplicates([1, 2, 2, 3, 3, 3, 4]))

# # Task 27: Reverse String

# # Write a function that reverses a string

# def reverse_string(text):
    
#     return text[::-1]

# # Test: reverse_string("hello") → "olleh"

# print(reverse_string("hello"))

# # Alternative

# def reverse_string(text):
    
#     reverse_str = ''
    
#     for i in range(len(text)):
#        i += 1
#        reverse_str += text[-i]
       
#     return reverse_str

# print(reverse_string("hello"))

# # Task 28: Count Vowels

# # Write a function that counts vowels (a, e, i, o, u) in a string
# def count_vowels(text):
    
#     vowels = 'aeiou'
    
#     cnt = 0
    
#     for i in text:
#         if i in vowels:
#             cnt += 1
    
#     return cnt

# # Test: count_vowels("hello") → 2

# print(count_vowels("hello"))

# # Task 29: Palindrome Check

# # Write a function that checks if a string is palindrome
# # Palindrome: reads the same forwards and backwards (e.g., "madam", "racecar")
# def is_palindrome(text):
    
#     if text == text[::-1]:
#         return True
#     else:
#         return False
    
# # Test: is_palindrome("madam") → True, is_palindrome("hello") → False

# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

# # Task 30: Count Words

# # Write a function that counts words in a string

# def count_words(text):
    
#     count = 0
    
#     for i in text.split(" "):
#         count += 1
        
#     return count

# # Test: count_words("Hello world from Python") → 4

# print(count_words("Hello world from Python"))

# # Task 31: Sum All

# # Write a function that takes any number of numbers and returns their sum

# def sum_all(*numbers):
    
#     total = sum(numbers)
    
#     return total

# # Test: sum_all(1, 2, 3) → 6, sum_all(10, 20, 30, 40) → 100

# print(sum_all(1, 2, 3))
# print(sum_all(10, 20, 30, 40))

# # Practice 1: Print Name

# # Write a function that prints your name

# def print_name():
#     print("Hello, Mokaddes Hossain")

# print_name()  # Output: আপনার নাম

# # Practice 2: Add 10

# # Write a function that takes a number and adds 10 to it

# def add_ten(num):
    
#     add_num = 10
    
#     return add_num + num

# print(add_ten(5))  # 15

# # Practice 3: Double It

# # Write a function that doubles a number

# def double(num):
    
#     return num * 2

# print(double(4))  # 8

# # Practice 4: Greet User

# # Write a function that takes a name and prints "Hi, [name]!"

# def greet(name):
    
#     print(f"Hi, {name}!")

# greet("Bob")  # Hi, Bob!

# # Practice 5: Is Positive?

# # Write a function that returns True if number is positive, False otherwise

# def is_positive(num):
    
#     return num > 0

# print(is_positive(5))   # True
# print(is_positive(-3))  # False

# # Practice 6: Subtract

# # Write a function that subtracts two numbers
# def subtract(a, b):
    
#     return a - b

# print(subtract(10, 3))  # 7

# # Practice 7: Divide

# # Write a function that divides two numbers
# def divide(a, b):
    
#     if b == 0:
#         return "Cannot dived by zero"
    
#     return a / b

# print(divide(10, 2))  # 5.0
# print(divide(10, 3))

# # Practice 8: Modulus

# # Write a function that returns remainder of division

# def remainder(a, b):
    
#     return a % b

# print(remainder(10, 3))  # 1

# # Practice 9: Convert Minutes to Hours

# # Write a function that converts minutes to hours

# def minutes_to_hours(minutes):
    
#     return minutes / 60

# print(minutes_to_hours(120))  # 2.0


# # Practice 10: Calculate Age

# # Write a function that takes birth year and returns age
# def calculate_age(birth_year):
    
#     present_year = 2024
    
#     return present_year - birth_year

# print(calculate_age(2000))  # 24

# # Practice 11: Odd or Even

# # Write a function that returns "Odd" or "Even"

# def odd_or_even(num):
    
#     return "Even" if num % 2 == 0 else "Odd"

# print(odd_or_even(4))  # Even
# print(odd_or_even(7))  # Odd




# Decorator

def store_decorator(my_func):
    
    def wrapper(name):
        
        print("Hi I am Coming your Shop")
        
        return my_func(name)
        
        print("Thank You for Coming")
        
    return wrapper



def buy_pet(pet_name):
    print(pet_name)
    

# buy_pet("Cat")
# buy_pet("Dog")

new_func = store_decorator(buy_pet)

new_func("Dog")

print()

print(new_func('Cat'))