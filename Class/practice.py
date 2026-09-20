# # Task 1: Grade Calculator

# # Function

# def grade_calculator(score):
    
#     if score > 100 or score < 0:
#         return "Invalid Input"
#     elif score >= 90:
#         return "90-100: A+"
#     elif score >= 80:
#         return "80-89: A"
#     elif  score >= 70:
#         return "70-79: B"
#     elif score >= 60:
#         return "60-69: C"
#     elif score >= 50:
#         return "50-59: D"
#     else:
#         return "Below 50: F"

 
# # Input from user

# score = int(input("Enter your score (0-100): "))

# print(grade_calculator(score))


# # Task 2: Leap Year Checker

# def leap_year_checker(year):
    
#     if year % 4 == 0 and year % 100 != 0:
#         return f"{year} is Leap Year"
#     elif year % 400 == 0:
#         return f"{year} is Leap Year"
#     else:
#         return f"{year} Not Leap Year"
    
# year = int(input("Enter a year: "))

# print(leap_year_checker(year))

# # Task 3: Triangle Type

# def triangle_type(a, b, c):
    
#     if a == b and a == c:
#         return f"Equilateral Triangle"
#     elif (a == b) or (a == c) and a != b != c:
#         return f"Isosceles Triangle"
#     else:
#         return f"Scalene Triangle"
        

# a = float(input("Side 1: "))
# b = float(input("Side 2: "))
# c = float(input("Side 3: "))

# print(triangle_type(a, b, c))

# # Task 4: Simple ATM

# balance = 1000
# print("1. Check Balance")
# print("2. Withdraw Money")
# print("3. Deposit Money")
# choice = int(input("Choose option: "))

# if choice == 1:
#     print(f"Your Balance: {balance}")
# elif choice == 2:
#     amount = float(input("Enter Your Amount: "))
#     if balance >= amount:
#         balance -= amount
#         print(f"{amount} Withdraw Successful, New Balance {balance}")
#     else:
#         print("Insufficient Balance")         
# elif choice == 3:
#     amount = float(input("Enter Your Amount: "))
#     balance += amount
#     print(f"{amount} Deposit Successful")
#     print(f"Balanced : {balance}")
    
# # Task 5: Prime Number Checker

# num1 = int(input())
# num2 = int(input())

# remainder = num1 % num2

# print(remainder)


