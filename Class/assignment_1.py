# #   1. Write a Python program to take your name and age as input and display them. 

# name = input("Enter Your Name: ")

# age = int(input("Enter Your Age: "))

# print(f"Name: {name} and Age: {age}. ")


# # 2. Write a program to calculate the average of three numbers.

# number_1 = float(input("Enter Your Number: "))
# number_2 = float(input("Enter Your Number: "))
# number_3 = float(input("Enter Your Number: "))

# avg_number = (number_1  + number_2 + number_3) / 3

# print(f"Average of three Number are {avg_number}")

# # Write a Python program to convert Celsius temperature to Fahrenheit. 

# celsius = float(input('Enter Celsius: '))

# fahrenheit = (celsius * 1.8) + 32

# print(f"Converted Temperature {celsius:.2f}°C = {fahrenheit:.2f}°F")

# # 4. Take two numbers as input and display addition, subtraction, multiplication, and division.

# num_1 = float(input("Number 1 : "))
# num_2 = float(input("Number 2 : "))

# # Display Addition

# print(f"Addition: {num_1 + num_2:.2f}")

# # Display Subtraction

# print(f"Subtraction: {num_1 - num_2:.2f}")

# # Display Multiplication

# print(f"Multiplication: {num_1 * num_2:.2f}")

# # Display Division
# if num_2 == 0:
#     print("Division: Cannot divide by zero!")
# else:
#     print(f"Division: {num_1 / num_2:.2f}")

# # 5. Create a list of 5 fruits and print the list. 

# mylist = ["Apple", "Banana", "Orange", "Kiwi", "Mango"]

# print(mylist)

# # 6. Create a dictionary containing student information and print it. 

# student = {
#     "name":"Md Mokaddes Hossain",
#     "age": 30,
#     "department": "CSE"    
# }

# print(student)

# # 7. Check whether a number is Positive, Negative, or Zero. 

# num = int(input("Enter Number: "))

# if num == 0:
#     print(f"This Number is 'Zero'.")
# elif num > 0:
#     print(f"This Number is 'Positive'.")
# elif num < 0:
#     print(f"This Number is 'Negative'.")
# else:
#     print("Invalid Input!!!!")

# # 8. Check whether a person is eligible for voting.

# print(" " * 30)

# age = int(input("Enter Your Age: "))

# print(" " * 30)

# print("=" * 30)

# if age >= 18:
#     print("You are eligible for voting.")
# else:
#     print("You are under age!!!")
    
# print("=" * 30)

# # 9. Print all even numbers from 1 to 20.

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# # 10. Find the sum of numbers from 1 to 10.

# total  = 0

# for i in range(1, 11):
#     total += i
# print(f"Total: {total}")

# # 11. Print the multiplication table of a number. 

# print()

# num = int(input("Enter Multiplication Number: "))

# print()

# print("=" * 30)

# print()

# for i in range(1, 11):
    
#     print(f"{num} x {i} = {num * i}")

# # 12. Find the factorial of a number. 

# num = int(input('Enter Number: '))

# factorial = num

# for i in range(1, num):
    
#    factorial *= num - i

# print(factorial)

# # 13. Create a simple password checker. Correct password: python123 

# password = input("Enter your password: ")

# c_pass = "python123"

# if password == c_pass:
#     print("Password Correct")
# else:
#     print("Wrong Password")
    

# # 14. Print all numbers from 1 to 50 that are divisible by 5. 
   
# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)

# # 15. Print numbers from 10 to 1 using range().

# for i in range(10, 0, -1):
    
#     print(i)

# # 16. Find the largest among three numbers. 

# num_1 = int(input("Number_1: "))
# num_2 = int(input("Number_2: "))
# num_3 = int(input("Number_3: "))

# #Use Max Function

# largest_number = max(num_1,num_2,num_3)

# print(f"Largest Number: {largest_number}")

# # 17. Check whether a number is Even or Odd.

# numbers = int(input("Enter Your Numbers: "))

# if numbers < 0:
#     print("Negative Number!!!")
# elif numbers % 2 == 0:
#     print("Even Number.")
# else:
#     print("Odd Number") 

# # 18. Create a grade calculator using if-elif-else. 

# marks = int(input("Enter Marks: "))

# if marks >= 80:
#     print("A+")
# elif marks  >= 70:
#     print("A")
# elif marks >= 60:
#     print("A-")
# elif marks >= 50:
#     print("B")
# elif marks >= 40:
#     print("C")
# elif marks >= 33:
#     print("D")
# else:
#     if marks < 0:
#         print("Invalid Marks!!!")
#     else:
#         print ("F")
        


# # 19. Print numbers from 1 to 10 but skip 5 using continue.

# for i in range(1, 11):
    
#     if i == 5:
#         continue
#     print((i)) 


# # 20. Print numbers from 1 to 10 but stop at 7 using break.

# for i in range(1, 11):
#     if i == 8:
#         break
#     print(i)

 
# # 21. Take a string input and print each character separately.

# my_str = input("Enter String: ")


# for i, word in enumerate(my_str):
#     print(f"{i + 1}: {word}") 
    
