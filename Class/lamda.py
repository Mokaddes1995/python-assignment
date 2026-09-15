# Task 1: Square Lambda

# Create a lambda function that returns the square of a number

square = lambda x : x ** 2

print(square(5))


# Task 2: Add Two Numbers

# Create a lambda function that adds two numbers

add = lambda a, b : a + b

print(add(10,20))


# Task 3: Check Even

# Create a lambda function that returns True if number is even

is_even = lambda x : x % 2 == 0

print(is_even(3))

print(is_even(4))


# Task 4: String Length

# Create a lambda function that returns the length of a string

length_string = lambda x : len(x)

print(length_string("This is a String"))


# Task 5: Max of Two

# Create a lambda function that returns the maximum of two numbers

max_num = lambda a, b : a if a > b else b

print(max_num(1,2))


# Task 6: Square All Numbers

# Use lambda with map() to square all numbers in a list

numbers = [1, 2, 3, 4, 5]

square_num = list(map(square, numbers))

print(square_num)


# Task 7: Convert to Uppercase

# Use lambda with map() to convert all strings to uppercase

names = ["alice", "bob", "charlie"]

uppercase_name = list(map(lambda x: x.upper(), names))

print(uppercase_name)


# Task 8: Double the Numbers

# Use lambda with map() to double all numbers in a list

numbers = [1, 2, 3, 4, 5]

double = list(map(lambda x : x * 2, numbers))

print(double)

# Task 9: Add Two Lists

# Use lambda with map() to add two lists element-wise

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]


extend_list = list(map(lambda x, y : x + y, list1, list2))

print(extend_list)


# Task 10: Convert Strings to Integers

# Use lambda with map() to convert strings to integers

str_nums = ["10", "20", "30", "40"]

new_list = list(map(lambda x : int(x), str_nums))

print(new_list)



# LEVEL 3: Lambda with filter() (টাস্ক ১১-১৫)

# Task 11: Filter Even Numbers

# Use lambda with filter() to get even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_num = list(filter(lambda x : x % 2 != 0, numbers))

print(odd_num)

# Task 12: Filter Numbers Greater Than 5

# Use lambda with filter() to get numbers greater than 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = list(filter(lambda x : x > 5, numbers))

print(num)


# Task 13: Filter Strings Starting with 'A'

# Use lambda with filter() to get strings starting with 'A'

names = ["Alice", "Bob", "Andrew", "Charlie", "Anna"]

name_with_a = list(filter(lambda x : x[0] == "A", names))

print(name_with_a)


# Task 14: Filter Non-Empty Strings

# Use lambda with filter() to remove empty strings

strings = ["Hello", "", "World", "", "Python"]

new_string = list(filter(lambda x : x.strip(''), strings))

print(new_string)


# Task 15: Filter Prime Numbers

# Use lambda with filter() to get prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = range(1, 50)


filtered = list(filter(lambda x: is_prime(x), numbers))

print(filtered)


#  PART 2: Decorator Tasks

# LEVEL 4: Basic Decorators (টাস্ক ১৬-২০)

# Task 16: Simple Logger

# Create a decorator that prints "Starting..." before a function and "Finished" after


def logger(func):
    
    def wrapper():
        
        print('Starting....')
        
        func()
        
        print('Finished')
        
    return wrapper


@logger
def greet():
    print("Hello!")
    
greet()


# Task 17: Uppercase Decorator

# Create a decorator that converts the return value to uppercase

def uppercase(func):
    
    def case_change():
        
        return func().upper()

    return case_change


@uppercase
def get_message():
    return "hello world"


print(get_message())  # HELLO WORLD


# Task 18: Repeat Decorator

# Create a decorator that repeats the function 3 times

def repeat(func):
    
    def wrapper():
        
        for i in range(3):
            func()
    return wrapper

@repeat
def greet():
    print("Hello!")


greet()

# Hello!
# Hello!
# Hello!


# Task 20: Exclaim Decorator

# Create a decorator that adds '!' at the end of the return value

def exclaim(func):
    
    def wrapper():
        
        result = func()
        
        return result + '!'
    
    return wrapper

@exclaim
def get_message():
    return "Hello"

print(get_message())  # Hello!


# LEVEL 5: Decorators with Arguments (টাস্ক ২১-২৫)

# Create a decorator that repeats a function N times

def repeat(n):
    
    def inner(func):
    
        def wrapper():
            
            for i in range(n):
            
                func()
            
        return wrapper
    
    return inner
    

@repeat(5)
def greet():
    print("Hello!")

greet()  # Hello! (5 times)

# Task 22: Add Prefix

# Create a decorator that adds a prefix to the return value

def add_prefix(prefix):
    
    def pass_func(func):
        
        def wrapper():
            
            result = prefix + func()
            
            return result
        
        return wrapper
    
    return pass_func

@add_prefix("Result: ")
def get_message():
    return "Success!"

print(get_message())  # Result: Success!


# Task 23: Validate Positive

# Create a decorator that validates if arguments are positive

def validate_positive(func):
    
    def wrapper(x, y):
        
                
        if y <= 0:
            return'Error'
        
        return func(x, y)     
        
    return wrapper

@validate_positive
def divide(a, b):
    return a / b

print(divide(10, 2))   # 5.0

# print(divide(10, -2))  # Error


# Task 24: Login Required

# Create a decorator that checks if user is logged in

def login_required(func):
        
    def wrapper(logged_in = False):
            
        if not logged_in:
            print("Access denied!")
        else:
        
            return func()
    
    return wrapper
 

@login_required
def view_profile():
    print("Viewing profile...")

view_profile(logged_in=True)   # Viewing profile...
view_profile(logged_in=False)  # Access denied!


# Task 25: Type Check

# Create a decorator that checks argument type

def type_check(str):
    
    def my_inner(func):
        
        def wrapper(text):
            
            if type(text) == str:
                            
                return func(text)
                            
            else:
                
                if type(text) == int:
                            
                    return "Error"
            
            
                
        return wrapper 
    return my_inner  

@type_check(str)
def process_text(text):
    return text.upper()

print(process_text("hello"))  # HELLO
print(process_text(123))     # Error


# 🏆 BONUS: Combined Tasks

# Apply two decorators: uppercase and exclaim

# Challenge 1: Multiple Decorators

def uppercase(func):
    
    def wrapper():
        
        result = func().upper()

        return result
    
    return wrapper

def exclaim(my_func):
    
    def my_inner():
        
        result = my_func() + '!'
        
        return result
    
    return my_inner

@uppercase
@exclaim
def get_message():
    return "hello"

print(get_message())  # HELLO!


# Challenge 2: Cache Decorator

# Create a cache decorator that stores results

def cache(func):
    
    cached = {}
    
    def wrapper(n):
        
        for n in cached:
            print(f"(cached) {n}")
            
            return cached[n]
        
        result = func(n)
        
        cached[n] = result
        
        return result
    
    return wrapper

@cache
def expensive_function(n):
    print(f"Calculating {n}")
    return n * n

print(expensive_function(5))  # Calculating 5, 25
print(expensive_function(5))  # (cached) 25