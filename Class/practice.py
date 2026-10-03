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


# # Practice 1 — String Slicing 🟢

# def first_half(string):
    
#     return string[: len(string)//2]


# string = input("Enter Text: ")

# result = first_half(string)

# print(result)


# # Practice 2 — Reverse 🟢

# def reverse_string(string):
    
#     return string[::-1]


# string = input("Enter Text: ")

# result = reverse_string(string)

# print(result)

# # Practice 3 — Every 3 Characters 🟡

# def wrap3(string):
    
#     result = ""
    
#     string_width = 3
    
#     for i in range((len(string)//string_width) + 1):
        
#         result += string[i * string_width : i * string_width + string_width] + "\n"
        
#     return result


# string = input("Enter Text: ")

# result = wrap3(string)

# print(result)


# # Practice 4 — Count Vowels 🟡

# def count_vowels(string):
    
#     vowels = "AEIOUaeiou"
#     count = 0
    
#     for i in string:
#         if i in vowels:
#             count += 1
            
#     return count


# string = input("Enter Text: ")

# result = count_vowels(string)

# print(result)        
        
        
# # Practice 5 — Find Maximum

# def find_max(numbers):
    
#     max_num = numbers[0]
    
#     for num in numbers:
        
#         if num > max_num:
#             max_num = num
    
#     return max_num



# numbers = [4, 9, 2, 15, 7]

# result = find_max(numbers)

# print(result)


# # Practice 6 — Count Characters

# def count_char(string, target):
    
#     count = 0
    
#     for i in string:
        
#         if i == target:
#             count += 1
            
#     return count


# string, target = input("Enter Text: "), input("Enter Text: ")

# result = count_char(string, target)

# print(result)


# # Practice 7 🟡 — Sum of Numbers

# def calculate_sum(numbers):
    
#     total = 0
    
#     for i in numbers:
        
#         total += i
        
#     return total
    

# numbers = [5, 10, 3, 7]

# result = calculate_sum(numbers)

# print(result)

# # Practice 8 — Find Minimum 🟡

# def find_min(numbers):
    
#     min_num = numbers[0]
    
#     for num in numbers:
        
#         if num < min_num:
            
#             min_num  = num
    
#     return min_num


# numbers = [8, 3, 12, 1, 7]

# result = find_min(numbers)

# print(result)


# # Practice 9 — Remove Duplicates 🟡🟠

# def remove_duplicates(numbers):
    
#     new_list = []
    
#     for i in numbers:
        
#         if i not in new_list:
            
#             new_list.append(i)
    
#     return new_list


# numbers = [1, 2, 2, 3, 1, 4, 3]

# result = remove_duplicates(numbers)

# print(result)



# # Practice 10 — Second Largest 🟠

# def second_largest(numbers):
    
#     max_num = float('-inf')
    
#     second_largest_num = float('-inf')
    
#     for num in numbers:
        
#         if num > max_num:
            
#             second_largest_num = max_num
            
#             max_num = num
            
#         elif num > second_largest_num:
            
#                 second_largest_num = num
                    
#     return second_largest_num
            


# numbers = [-2, -5, -1, -8]

# result = second_largest(numbers)

# print(result)


# # Practice 11 — Find Common Elements 🟠

# def common_elements(list1, list2):
    
#     common = []
    
#     for i in list1:
        
#         for j in list2:
            
#             if i == j:
                
#                 if i not in common:
#                     common.append(i)
                
#     return common


# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 5, 7, 9]

# result = common_elements(list1, list2)

# print(result)

# # Practice 12 — Palindrome 🟠

# def is_palindrome(string):
    
#     new_str = ''
    
#     for i in range(1,len(string) + 1):
    
#         new_str += string[-i]
        
#     return string == new_str


# string = input("Enter Text: ")

# result = is_palindrome(string)

# print(result) 

# # Practice 13 — Second Smallest 🟠

# def second_smallest(numbers):
    
#     lowest = float("inf")
    
#     second_small = float('inf')
    
#     for num in numbers:
        
#         if num < lowest and num != lowest:
            
#             second_small = lowest
            
#             lowest = num
        
#         elif num < second_small :
#             second_small = num
            
#     return second_small
    

# numbers = [5, 5, 8, 10]

# result = second_smallest(numbers)

# print(result) 

# # Practice 14 — Frequency Counter 🟠

# def frequency_count(string):
    
#     freq = {}
    
#     for i in string:
        
#         if i in freq:
            
#             freq[i] += 1
#         else:
#             freq[i] = 1     
    
#     return freq



# string = input("Enter Text: ")

# result = frequency_count(string)

# print(result) 


# # Practice 15 — Most Frequent Character 🟠

# def most_frequent(string):
    
#     freq =  {}
    
#     for i in string:
        
#         if i in freq:
            
#             freq[i] += 1
#         else:
#             freq[i] = 1
    
#     max_count = 0
#     most_char = ""

#     for char, count in freq.items():
        
#         if count > max_count:
#             max_count = count
#             most_char = char
        
#     return most_char


# string = "banana"

# result = most_frequent(string)

# print(result) 


# Practice 16 — First Non-Repeating Character 🟠

def first_non_repeating(string):
    
    freq = {}
    
    for i in string:
        
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
            
    
    for char, count in freq.items():
        
        if count == 1:
            
            return f"{char} -> {count}"
        
    return f"No Repeating Char"
    
string = "aaebbc"

result = first_non_repeating(string)

print(result)