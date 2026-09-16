# # Section 1: Programming Tasks

# # Task 1 (Basic Class): Create a class named Laptop with properties for brand, processor, and price. 
# # Create an object of this class and print all its details.

# class Laptop:
    
#     # Constructor Method
    
#     def __init__(self, brand, processor, price):
#         self.brand = brand
#         self.processor = processor
#         self.price = price
        
#     # Instance Method for Printing Information
    
#     def display_info(self):
        
#         print(f"Brand: {self.brand}")
#         print(f"Processor: {self.processor}")
#         print(f"Price: {self.price}")
        
    
# # Create an Object Named Laptop1

# laptop1 = Laptop("Asus", "Intel Core i7", 190000)

# # Call Object Method for Display Information

# laptop1.display_info()


# # Task 2

# ''' 
# Task 2 (Method Implementation): Create a class Circle that takes radius as a parameter in the __init__ method. 
# Add a method called calculated_area that returns the area of the circle (Formula: π𝑟2  ) and a  method called 
# calculated_perimeter that returns the perimeter of the circle (Formula: 2πr).
# '''

# # Import Math Module for pi

# import math

# class Circle:
    
#     # Constructor Method
    
#     def __init__(self, radius):
        
#         # Take Radius Parameter
        
#         self.radius = radius
        
#     # Instance Method for Calculated Area
    
#     def calculated_area(self):
        
#         area = math.pi * self.radius ** 2
        
#         return area
    
#     # Instance Method for Calculated Perimeter
    
#     def calculated_perimeter(self):
        
#         perimeter = 2 * math.pi * self.radius
        
#         return perimeter
    
#     # Instance Method for Show Information
    
#     def show_information(self):
        
#         # Call Calculated Area Method
        
#         print(f"Area: {self.calculated_area():.6f}")
        
#         # Call Calculated Perimeter Method 
        
#         print(f"Perimeter: {self.calculated_perimeter():.6f}")
        

# "Create an Object"

# circle1 = Circle(50)

# # Display Information

# circle1.show_information()


# # Task 3

# '''
# Task 3 (Object Manipulation): Create a Player class with name and score. 
# Create an object, print the initial score, update the score with new value, and print the updated score.
# '''

# class Player:
    
#     # Constructor Method
    
#     def __init__(self, name, score):
        
#         self.name = name
#         self.score = score
        
#     # Create Instance Method for Update Score
    
#     def update_score(self, new_score):
        
#         # Give Validation for Negative Value
        
#         if new_score < 0:
            
#             raise ValueError ('Score Must Be 0 and Above!!')
            
#         # Update Score with New Score
            
#         self.score = new_score
            
#         print(f"Updated Score: {self.score}")
    
#     # Instance Method for Printing Information
    
#     def show_info(self):
        
#         print(f"Name: {self.name}")
#         print(f"Score: {self.score}")
        
    
# # Create an Object

# player1 = Player('Mahir', 30)

# # Print Name and Initial Score

# player1.show_info()

# # Print Updated Score

# player1.update_score(60)


# # Task 4

# '''
# Task 4 (Conditional Logic): Create a Temperature class. If the input 
# temperature is above 37°C, the method check_health should print 
# “Fever”, otherwise “Normal”
# '''

# class Temperature:
    
#     # Constructor Method
    
#     def __init__(self, temp):
        
#         self.temperature = temp
        
#     # Instance Method for Check Health
    
#     def check_health(self):
        
#         if self.temperature > 37:
#             print("Fever")
#         else:
#             print('Normal')
            
# # Take Input for Temperature

# temp = float(input('Enter Your Temperature: '))

# # Create an Object

# temperature1 = Temperature(temp)

# # Call Check Health

# temperature1.check_health()


# # Task 5

# '''
# Task 5 (Inheritance): Create a parent class Vehicle with a method move().
# Create a child class Airplane that inherits from Vehicle and adds a unique method fly().
# '''

# # Create Parent Class Vehicle

# class Vehicle:
    
#     # Instance Method
    
#     def move(self):
        
#         print("The vehicle is moving.")



# # Create Child Class Airplane

# class Airplane(Vehicle):    # Inheritance Vehicle Class
    
#     # Instance Method
    
#     # Unique Method fly
    
#     def fly(self):
        
#         print("The Airplane Flying")
        

# # Create an Object

# airplane1 = Airplane()

# # Call Inheritance Method

# airplane1.move()

# # Call Unique Method

# airplane1.fly()


# Section 2: Scenario-based Challenges

'''

ATM System: Create a class named Class. The account should contain: 
Account number, Account holder name, Balance. Implement the following 
methods: deposit(), withdraw(), show_balance(). The system must: 
○  Allow users to deposit and withdraw money. 
○  Prevent withdrawal when the balance is insufficient. 
○  Display the current balance. 
○  Create at least two different accounts. 
○  Perform transactions on both accounts. 

'''

class BankAccount:
    
    # Constructor Method
    
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.account_holder_name = name
        self.__balance = balance            # Encapsulation Method for Private Balance
        
    # Instance Method 
    
    # Method Show Balance
    
    def show_balance(self):
        print(f"Balance: {self.__balance:.2f}")
        
    # Method Deposit Balance
    
    def deposit(self, amount):
        
        # Validation for O and Negative amounts
        
        if amount <= 0:
            raise ValueError("Amount Must be 1 and above!!")
        
        
        self.__balance += amount
        
        print(f"${amount:.2f} Deposit Successful..")
        
        self.show_balance()
        
        
    # Method Withdraw Balance
    
    def withdraw(self, amount):
        
        # Validation for 0 and Negative amounts
        
        if amount <= 0:
            raise ValueError ("Amount Must be 1 and above!!")
        
        # Prevent withdrawal when the balance is insufficient.
        
        if amount > self.__balance:
            raise ValueError ('Insufficient Balance!!!')
        
        self.__balance -= amount
        
        print(f"${amount:.2f} Withdraw Successful..")
        
        self.show_balance()
    


# Create two different accounts.

ba1 = BankAccount(13456, "Md Mokaddes Hossain", 5000)

ba2 = BankAccount(13457, "Maimun Al Rafat", 10000)

# Display the current balance

ba1.show_balance()
ba2.show_balance()

# Deposit Money with Error Handling

try:
    ba1.deposit(5000)
    
except ValueError as e:
    
    print(e)
    

try:
    ba2.deposit(3000)
    
except ValueError as e:
    
    print(e)
    
    
# Withdraw Money with Error Handling

try:
    ba1.withdraw(7000)
    
except ValueError as e:
    
    print(e)
    

try:
    ba2.withdraw(12000)
    
except ValueError as e:
    
    print(e)
    
    


'''
Library Management System: Create two classes named Book and Library. 
In Book class, each book should contain: Title, Author, ISBN, Availability Status. 
In Library class, the library should provide methods to: 
add_method(), borrow_book(), return_book(), display_books(). The 

system should: 
○  Allow books to be added to the library. 
○  Display all available books. 
○  Allow user to borrow a book 
○  Prevent a book from being borrowed if it is already borrowed. 
○  Allow borrowed books to be returned. 
○  Update the availability status automatically. 
'''

# Create Book Class

class Book:
    
    # Constructor Method
    
    def __init__(self, title, author, isbn, is_availability):
        
        self.title = title
        self.author = author
        self.isbn = isbn
        
        self.is_available = True  
        


# Create Library Class

class Library():
    
    # Constructor Method
    
    def __init__(self):
        
        self.books = []
    
            
    # Instance Method
    
    # Method Add
    
    def add_method(self, book):
        
        self.books.append(self.book)
    
    # Method borrow book
    
    def borrow_book(self, isbn):
        
        for book in self.books:
            
            if book.isbn == isbn:
            
                if self.is_availability:
                
                    self.is_availability = False
                
                    print("Borrow the Book")
                
                else:
                
                    print("Already borrowed")
        
    # Method return book
    
    def return_book(self):
        
        if not self.is_availability:
            
            self.is_availability = True
            
            print("Book Return")
            
        else:
            
            print("The Book Already Returned!!!")
    
    
    # Method display book
    
    def display_books(self):
        
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available:{self.is_availability}")
        
        
# Crate Library Object

book1 = Library('Python Programming', 'Jon Luise', 'A12756B', True)

book1.display_books()

book1.add_method('Python', 'John Doe', 'A12756B', True)

book1.display_books()
        