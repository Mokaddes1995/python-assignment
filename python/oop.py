
# Create Class 

# class Car:
    
#     Brand = 'Toyota'
    
    
#     def __init__(self, model, color):
        
#         self.model = model
#         self.color = color
        
    
#     def show_info(self):
        
#         print(f"Brand: {self.Brand}")
#         print(f"Model: {self.model}")
#         print(f"Color: {self.color}")
        
#     @classmethod
#     def update_company_nam(cls, new_name):
        
#         cls.Brand = new_name
        
        
# car1 = Car('Corola', 'White')

# car2 = Car('Hiace', 'Black')

# car1.show_info()

# Car .update_company_nam('Honda')

# car1.show_info()
# car2.show_info()


# #  1. Student Management System

# class Student:
    
#     # __init__ Method
    
#     def __init__(self, name, id, marks):
        
#         self.name = name
#         self.id = id
#         self.marks = marks
        
#     # Instance Method
        
#     def displayInfo(self):
        
#         print(f"Student ID: {self.id}")
        
#         print(f"Name: {self.name}")
        
#         print(f"Marks : {self.marks}")
        
#         print(f"You Got : {self.calculateGrade()}")
        
    
#     def calculateGrade(self):
        
#         if self.marks >= 80:
#             return 'A+'
#         elif self.marks >= 70:
#             return 'A'
#         elif self.marks >= 60:
#             return 'A-'
#         elif self.marks >= 50:
#             return "B"
#         elif self.marks >= 40:
#             return 'C'
#         elif self.marks >= 33:
#             return "D"
#         else:
#             return "Fail"
        

# s1 = Student("Rahim", 1, 90)

# s2 = Student('Karim', 2, 80)

# s3 = Student('Mahin', 3, 86)

# s1.displayInfo()


# # 2. Bank Account

# class BankAccount:
    
#     # Constructor or __init__ Method
    
#     def __init__(self,accountNumber, ownerName, balance):
        
#         self.accountNumber = accountNumber
#         self.ownerName = ownerName
#         self.balance  = balance
        
    
#     # Instance Method
    
#     def deposit(self, amount):
        
#         if amount <= 0:
            
#             raise ValueError ('Amount must be 1 and above')
        
#         self.balance += amount
        
#         print(f"{amount} Deposited Successful")
#         print(f"New Balance : {self.balance}")
        
    
#     def withdraw(self, amount):
        
            
#         if amount <= 0 or amount > self.balance:
                
#             raise ValueError ('Insufficient Balance Or Invalid Amount')
        
#         self.balance -= amount
        
#         print(f"{amount} Withdraw Successful")
#         print(f"New Balance : {self.balance}")
        
        
#     def checkBalance(self):
        
#         print(f'Balance: {self.balance}')
        
        
# ba1 = BankAccount(12345, "Rahim", 7000 )

# try:
#     ba1.deposit(2000)
# except Exception as e:
#     print(f"Error {e}")

# try:
#     ba1.withdraw(10000)
# except Exception as e:
#     print(f"Error {e}")


# # 3. Car Class

# class Car:
    
#     # Constructor Method
    
#     def __init__(self, brand, model, speed):
        
#         self.brand = brand
        
#         self.model = model
        
#         self.is_start = False
        
#         self.speed = speed
        
#     # Instance Method
    
#     def accelerate(self):
        
#         if self.is_start:
#             print('Car Already Started')
#         else:
            
#             if not self.is_start:
#                 print('Car is Start')
#                 self.speed += 10
#                 print(f'Car is Accelerate.....Speed is {self.speed}')
                
    
#     def brake(self):
        
#         if self.is_start:
#             print(f"Engine Off")
#             print(f"Car Strat First")
#         else:
#             if not self.is_start:
#                 self.speed -= 5
#                 print(f'Break !!!!! Car Speed {self.speed}')
        
                
#     def displayStatus(self):
        
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")  

# # Task 1 — Class & Object

# class Student:
    
#     def display_info(self):
        
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Department: {self.department}")


# s1 = Student()

# s2 = Student()

# s3 = Student()

# s1.name = 'Rahim'
# s1.age = 30
# s1.department = 'CSE'

# s1.display_info()

# s2.name = 'Karim'
# s2.age = 32
# s2.department = 'BBA'

# s2.display_info()

# s3.name = 'Rakib'
# s3.age = 31
# s3.department = 'EEE'

# s3.display_info()

# # Task 2 — Constructor

# class Book:
    
#     # Constructor Method
    
#     def __init__(self, title, author, price):
        
#         self.title = title
#         self.author = author
#         self.price = price
        
    
#     # Instance Method
    
#     def display_info(self):
        
#         print(f"Title Name: {self.title}")
#         print(f"Author Name: {self.author}")
#         print(f"Price: {self.price}")
#         print(f"Discount Price: {self.discount()}")
        
    
#     def discount(self, dis_percent = 10):
        
#         discount_price = self.price - (self.price * dis_percent /100)
        
#         return discount_price
    
    
# book1 = Book('Learn Python', 'Mark Luis', 1000)
# book2 = Book('MySql Basic', 'Zamir Mamdani', 900)

# book1.display_info()
# book2.display_info()

# # Task 3 — Encapsulation

# class BankAccount:
    
#     # Constructor Method
    
#     def __init__(self, account_number, balance):
        
#         self.__account_number = account_number
#         self.__balance = balance
    
#     # Getter Method
    
#     def get_balance(self):
        
#         return f"Balance: ${self.__balance}"  
    
    
#     def deposit(self, amount):
        
#         if amount <= 0:
#             raise ValueError ('Amount must be greater than 0!!')
        
#         self.__balance += amount
        
#         print(f"${amount} is deposited successful..")
#         print(f"New {self.get_balance()}")
        
        
    
#     def withdraw(self, amount):
        
#         if amount <= 0 or amount > self.__balance:
#             raise ValueError ("Amount must be greater than 0 or Insufficient Balance!!!")
        
#         self.__balance -= amount
        
#         print(f"${amount} is Withdraw successful")
#         print(f"New {self.get_balance()}")

        


# ba1 = BankAccount(1234, 5000)
# ba2 = BankAccount(4321, 4000)

# print(ba1.get_balance())

# ba1.deposit(5000)

# ba1.withdraw(2000)


# # Task 1: Bank Account (Basic Encapsulation)

# # Create a BankAccount class with:
# # - Private attribute: __balance
# # - Public methods: deposit(), withdraw(), get_balance()
# # - Validate: cannot withdraw more than balance

# class BankAccount:
    
#     # __init__ Method
    
#     def __init__(self, balance):
        
#         self.__balance = balance
        
#     # Public Method
    
    
#     # Instance Method for Deposit Amount
    
#     def deposit(self, amount):
        
#         # Validation for 0 or Negative Amount
        
#         if amount <= 0:
#             raise ValueError ("Amount must be 1 or Higher")
        
#         self.__balance += amount
        
#         print(f"Balance: {self.get_balance()}")
        
#     # Withdraw Amount
    
#     def withdraw(self, amount):
        
#         # Validation for O and cannot withdraw more than balance
        
#         if amount <= 0:
#             raise ValueError ('Invalid Amount!!!!')
        
#         elif amount > self.__balance:
#             raise ValueError('Insufficient Balance!!!!')
        
#         else:
#             self.__balance -= amount
            
#         print(f"Balance: {self.get_balance()}")
            
        
#     # Get Balance
    
#     def get_balance(self):
        
#         return self.__balance    

# # Test:
# acc = BankAccount(1000)
# acc.deposit(500)      # Balance: 1500
# acc.withdraw(200)     # Balance: 1300
# # acc.withdraw(2000)    # Error: Insufficient balance!
# print(acc.get_balance())  # 1300


# # Task 2: Student (Private Attributes)

# # Create a Student class with:
# # - Private attributes: __name, __roll, __marks
# # - Getter and Setter methods
# # - Validate: marks between 0-100

# class Student:
    
#     # __init__ Method
#     def __init__(self, name, roll, marks):
        
#         self.__name  = name
#         self.__roll = roll
#         self.set_marks(marks)
        
#     # Getter Method
    
#     def get_name(self):
#         return f"Name: {self.__name}"
    

#     def get_marks(self):
#         return f"Marks: {self.__marks}"
    
#     # Setter Method
    
#     def set_marks(self, mark):
        
#         # Validate marks between 0-100
        
#         if mark >= 0 and mark  <= 100:
#             self.__marks = mark
#         else:
#             raise ValueError ("Error: Marks between 0-100")
    

# # Test:
# s = Student("Alice", 101, 85)
# print(s.get_name())    # Alice
# s.set_marks(95)
# print(s.get_marks())   # 95
# s.set_marks(150)       # Error: Marks must be between 0-100!


# # Task 3: Employee (Salary Encapsulation)

# # Create an Employee class with:
# # - Private: __name, __salary
# # - Method: calculate_bonus() (10% of salary)
# # - Setter with validation (salary cannot be negative)

# class Employee:
    
#     # Constructor Method
    
#     def __init__(self, name, salary):
        
#         self.__name = name
#         self.__salary = salary
        
#     # Instance Method
    
#     # Getter Method
    
#     def get_name(self):
        
#         return self.__name
    
#     def get_salary(self):
        
#         return self.__salary
    
#     # Setter Method
    
#     def set_salary(self, amount):
        
#         # Validation (salary cannot be negative)
        
#         if amount < 0:
#             raise ValueError ("Salary cannot be negative or 0")
        
#         self.__salary = amount
        
    
#     # Calculate Bonus
    
#     def calculate_bonus(self, percent = 10):
        
#         bonus = self.__salary * percent/100
        
#         return bonus
    
#     def display_info(self):
#         print(f"Name: {self.get_name()}")
#         print(f"Salary: {self.get_salary()}")
    


# # Test:
# emp = Employee("Bob", 50000)
# print(emp.get_salary())      # 50000
# print(emp.calculate_bonus()) # 5000.0
# emp.set_salary(60000)
# print(emp.get_salary())      # 60000
# emp.set_salary(-1000)        # Error: Salary cannot be negative! 


# # Task 4: Library Book

# # Create a Book class with:
# # - Private: __title, __author, __is_available
# # - Methods: borrow(), return_book(), is_available()

# class Book:
    
#     # Constructor Method
    
#     def __init__(self, title, author):
        
#         self.__title = title
#         self.__author = author
#         self.__is_available = True
        
    
#     # Instance Method
    
#     # Getter Method
    
#     def get_title(self):
        
#         return self.__title
    
#     def get_author(self):
        
#         return self.__author
    
    
#     # Setter Method
    
#     def set_title(self, new_title):
        
#         self.__title = new_title
        
#         return self.__title
    
#     def set_author(self, new_author):
        
#         self.__author = new_author
        
#         return self.__author
    
    
#     # Method
    
#     def is_available(self):
        
#         return self.__is_available
        
    
#     def borrow(self):
        
#         if self.__is_available:
            
#             self.__is_available = False
#             print("Book borrowed")
            
#         else:
            
#             raise ValueError ("Error: Book not available")
        
#     def return_book(self):
        
#         if not self.__is_available:
#             self.__is_available = True
#             print('Book returned')
#         else:
#             print("Book Already Available")  
  

# # Test:
# book = Book("Python Programming", "John Doe")
# print(book.is_available())  # True
# book.borrow()               # Book borrowed
# print(book.is_available())  # False
# # book.borrow()               # Error: Book not available
# book.return_book()          # Book returned
# print(book.is_available())  # True


# # Task 5: Temperature Converter

# # Create a Temperature class with:
# # - Private: __celsius
# # - Getter: get_celsius(), get_fahrenheit()
# # - Setter: set_celsius(), set_fahrenheit()
# # - Validate: absolute zero (-273.15°C)

# class Temperature:
    
#     # Constructor Method
    
#     def __init__(self, celsius):
        
#         self.__celsius = celsius
        
#     # Instance Method
    
#     # Getter Method
    
#     def get_celsius(self):
        
#         return f"Temperature: {self.__celsius}°C"
    
#     def get_fahrenheit(self):
        
#         fahrenheit = (self.__celsius * 9/5) + 32
        
#         return f"Fahrenheit: {fahrenheit}°F"
    
#     # Setter Method
    
#     def set_celsius(self, new_celsius):
        
#         if new_celsius < -273.15:
            
#             raise ValueError ("absolute zero (-273.15°C)")
#         else:
#             self.__celsius = new_celsius
        
    
#     def set_fahrenheit(self, new_fahrenheit):
        
#         if new_fahrenheit > -459.67:
            
#             raise ValueError ("absolute zero") 
          
#         else:
#             celsius = (new_fahrenheit - 32) * 5/9
            
#             return f"Celsius: {celsius}°C"
            
        
    

# # Test:
# temp = Temperature(25)
# print(temp.get_celsius())     # 25
# print(temp.get_fahrenheit())  # 77.0
# temp.set_celsius(30)
# print(temp.get_celsius())     # 30
# temp.set_celsius(-300)        # Error: Below absolute zero!


# Task 1: Bank Account System

# Requirements:

# Base Class: Account

class Account:

    # Private: __account_number, __balance
    
        # Constructor Method
    
    def __init__(self, account_number, balance):
        
        self.__account_number = account_number
        self.__balance = balance


    # Public methods: deposit(amount)
    
    def deposit(self, amount):
        
        # Validation: deposit > 0
        
        if amount <= 0:
            
            raise ValueError ("Invalid Amount!! Amount must be greater than 0!!")

        else:
            self.__balance += amount
            
            print(f"${amount} Deposit Successful..")
            
            print(f"New {self.get_balance()}")
            
     
    # Public methods:withdraw(amount)
    
    def withdraw(self, amount):
        
        # Validation: withdraw ≤ balance
        
        if amount <= 0: 
            
            raise ValueError ("Invalid Amount!!!")
        
        elif amount > self.__balance:
            
            raise ValueError ("Insufficient Balance!!")
        
        else:
            
            self.__balance -= amount
            
            print(f"${amount} Withdraw Successful..")
            
            print(f"New {self.get_balance()}")              
    
    # Public methods:get_balance()
    
    def get_balance(self):
        
        return f"Balance: {self.__balance}"
    
    # Protected helper methods
    
    def _get_balance(self):
        return self.__balance

    def _set_balance(self, balance):
        self.__balance = balance


# Child Class: SavingsAccount(Account)

class SavingsAccount(Account):
    
    # Additional attribute: interest_rate
    
    def __init__(self, account_number, balance, rate):
        
        super().__init__(account_number, balance)
        
        self.interest_rate = rate
    

    # Method: add_interest() — balance + (balance × interest_rate / 100)
    
    def add_interest(self):
        
        balance = self._get_balance()
        
        interest = balance * self.interest_rate /100
        
        self._set_balance(balance + interest)
        
        return f"{self._get_balance()} With {self.interest_rate}% Interest"
    
    
    # Method For Change Interest Rate
    
    def change_interest(self, new_rate):
        
        if new_rate <= 0:
            
            raise ValueError ('Interest rate must be grater than 0!!')
        
        self.interest_rate = new_rate


# Child Class: CurrentAccount(Account)

class CurrentAccount(Account):

    # Additional attribute: overdraft_limit
    
    def __init__(self, account_number, balance, amount):
        
        super().__init__(account_number, balance)
        
        self.overdraft_limit = amount

    # Override withdraw() — overdraft limit পর্যন্ত withdraw করা যাবে
    
    def withdraw(self, amount):
        
        balance = self._get_balance()
        
        # Validation for Over Draft Limit
        
        if amount <= 0: 
                    
            raise ValueError ("Invalid Amount!!!")
                
        else:
            
            over_draft_amount = balance + self.overdraft_limit
                
            if amount > over_draft_amount:
                
                raise ValueError ("Insufficient Balance. You Exceed Overdraft Limit Also !!!")

            else:
                    
                balance -= amount
                    
                print(f"${amount} Withdraw Successful..")
                
                self._set_balance(balance)
                    
                print(f"New {self.get_balance()}")
    
                
    # Method For Change Over Draft Limit
        
    def change_overdraft_limit(self, new_amount):
        
        if new_amount <= 0:
            raise ValueError ("Over Draft Amount Must be grater than 0!!")
            
        self.overdraft_limit = new_amount    


from datetime import datetime

# Child Class: FixedDepositAccount(Account)

class FixedDepositAccount(Account):  

    # Additional attribute: maturity_years
    
    def __init__(self, account_number, balance, year):
        
        super().__init__(account_number, balance)
        
        self.maturity_year = year
        
        self.start_date = datetime.now().year
        
        self.maturity_year = self.start_date + self.maturity_year
        
        
    # Check Maturity
    
    def is_maturity(self):
        
        current_year = datetime.now().year
        
        return current_year >= self.maturity_year
        

    # Override withdraw() — maturity এর আগে withdraw করা যাবে না
    
    def withdraw(self, amount):
            
        # Validation for Over Draft Limit
        
        if not self.is_maturity():
            
            years_left = self.maturity_year - datetime.now().year
            
            raise ValueError (f"Your Fixed Deposit Not Mature!! {years_left} years left.")
        
                
        if amount <= 0: 
                            
            raise ValueError ("Invalid Amount!!!")

        balance = self._get_balance()

        if amount > balance:
                                    
            raise ValueError ("Insufficient Balance. You Exceed Overdraft Limit Also !!!")
                        
        balance -= amount
                            
        self._set_balance(balance)
                            
        print(f"${amount} Withdraw Successful..")
        print(f"New {self.get_balance()}")
        
                    
    # Method For Change Maturity Year
            
    def change_maturity_year(self, new_year):
        
        if new_year <= 0:
            
            raise ValueError ('Maturity Year Must Be Grater than 0')
                
        self.maturity_year = datetime.now().year + new_year 


accounts = [
    SavingsAccount("SA001", 1000, 5),
    CurrentAccount("CA001", 2000, 500),
    FixedDepositAccount("FD001", 5000, 3)
]

for acc in accounts:
    
    try:
        acc.deposit(5000)
    except Exception as e:
        print(e)
    
    try:
        acc.withdraw(200)
    except Exception as e:
        print(e)
        
    print(acc.get_balance())   