from datetime import datetime

# # Task 1: Student Report Card

# students = []

# for _ in range(int(input("Enter Number Of Student: "))):
    
    
#     name = input(f"Student {_+1} Name: ")
    
#     marks = list(map(int, input("Enter 3 marks: ").split()))
    
#     # Total Marks

#     total_marks = sum(marks)
    
#     # Average Marks

#     average = sum(marks) /len(marks)
    
#     # Grade

#     if average >= 80:
#         grade = "A+"
#     elif average >= 70:
#         grade = "A"
#     elif average >= 60:
#         grade = "B"
#     elif average >= 33:
#         grade = "C"
#     else:
#         grade = 'F'
    
#     student = {
#         "name": name,
#         'marks': marks,
#         'total': total_marks,
#         'average': average,
#         'grade' : grade
#     }
    
#     students.append(student)    
    

# # Report Card

# print("=" * 10 + " " + "Report Card" + " " + "=" * 10)

# for s in students:
    
#     print(f"Name : {s['name']}")
#     print(f"Marks: {s['marks']}")
#     print(f"Total: {s['total']}")
#     print(f"Average: {s['average']:.2f}")
#     print(f"Grade: {s['grade']}")
    
#     print('-' * 20)
    
# print("=" * 32)

# class_average = sum(s['average'] for s in students)/ len(students)

# print(f"Class Average: {class_average:.2f}")

# top = max(students, key=lambda s: s['average'])

# print(f"Top Student: {top['name']}({top['average']:.2f})")


# Task 2: Bank Account System (OOP)

# Base Class Account

class Account:
    
    # Constructor Method
    
    def __init__(self, account, balance):
        
        self.__account_number = account
        self.__balance = balance
        
    # Instance Method for deposit
    
    def deposit(self, amount):
        
        if amount <= 0 :
            raise ValueError ("Invalid Amount!! Amount must be grater than 0!!!")
        
        self.__balance += amount
        
        print(f"{amount} deposit Successful...New Balance: {self.get_balance()}")
        
    
    # Instance Method for Withdraw
    
    def withdraw(self, amount):
        
        if amount  <= 0:
            raise ValueError ("Invalid Amount!!  Amount must be grater than 0!!")
        
        if amount > self.__balance:
            raise ValueError("Insufficient Balance!!!")
        
        self.__balance -= amount
        
        print(f"{amount} Withdraw Successful...New Balance: {self.get_balance()}")
        
        
        
    
    # Instance Method for Access Balance
    
    def get_balance(self):
        
        return self.__balance
    
    def set_balance(self, balance):
        
        self.__balance = balance
      
    
# Child Class: SavingsAccount(Account)

class SavingsAccount(Account):
    
    # Constructor Method with Super() use
    
    def __init__(self, account, balance, rate):
        
        super().__init__(account, balance)
        
        self.interest_rate = rate
        
    
    # Instance Method
    
    def add_interest(self):
        
        balance = self.get_balance()
        
        balance += (balance * self.interest_rate/100)
        
        self.set_balance(balance)
        

# Child Class: CurrentAccount(Account)

class CurrentAccount(Account):
    
    # Constructor Method With Super()
    
    def __init__(self, account, balance, limit):
        super().__init__(account, balance)
        
        self.overdraft_limit = limit
    
    # Overdraft withdraw
    
    def withdraw(self, amount):
        
        balance = self.get_balance()
            
        if amount  <= 0:
            raise ValueError ("Invalid Amount!!  Amount must be grater than 0!!")
            
        if amount > balance + self.overdraft_limit:
            raise ValueError("Insufficient Balance!!!")
            
        balance -= amount
        
        self.set_balance(balance)
            
        print(f"{amount} Withdraw Successful...New Balance: {self.get_balance()}")


# Child Class: FixedDepositAccount(Account)

class FixedDepositAccount(Account):
    
    # Constructor Method with Super()
    
    def __init__(self, account, balance, year):
        super().__init__(account, balance)
                
        self.maturity_year = 3
        
        self.start_year = datetime.now().year
        
        self.maturity = self.start_year + self.maturity_year
        
    # Maturity Validation
    
    def is_maturity(self):
        
        return self.maturity <= datetime.now().year

    
    # Withdraw Method override
    
    def withdraw(self, amount):
        
        balance = self.get_balance()
                
        if amount  <= 0:
            raise ValueError ("Invalid Amount!!  Amount must be grater than 0!!")
        
        if not self.is_maturity():
            
            years_left = self.maturity - datetime.now().year
            
            raise ValueError(f"FD not mature yet! {years_left} years left.")

               
        if amount > balance :
            raise ValueError("Insufficient Balance!!!")
                       
        
        balance -= amount
            
        print(f"{amount} Withdraw Successful...New Balance: {self.get_balance()}")
        
        self.set_balance(balance)
                
        
        
        
        
accounts = [
    SavingsAccount("SA001", 1000, 5),
    CurrentAccount("CA001", 2000, 500),
    FixedDepositAccount("FD001", 5000, 3)
]

for acc in accounts:
    
    print(f"\n--- {acc.__class__.__name__}---")
    
    try:
        acc.deposit(100)
        
        acc.withdraw(200)
        
        print(f"Balance: {acc.get_balance()}")
        
    except ValueError as e:
        
        print(f"Error: {e}")       
        

        
        
        

