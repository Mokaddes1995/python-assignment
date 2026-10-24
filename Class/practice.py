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


# # Practice 16 — First Non-Repeating Character 🟠

# def first_non_repeating(string):
    
#     freq = {}
    
#     for i in string:
        
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
            
    
#     for char, count in freq.items():
        
#         if count == 1:
            
#             return f"{char} -> {count}"
        
#     return f"No Repeating Char"
    
# string = "aaebbc"

# result = first_non_repeating(string)

# print(result)



# # Exercise 1 — Positive or Negative

# number = int(input("Enter a number: "))

# if number >= 0:
#     print("Positive Number")
# else:
#     print("Negative Number")



# # Exercise 2 — Multiplication Table

# n = int(input("Enter a number: "))

# for i in range(1, 11):
    
#     print(f"{n} x {i} = {n * i}")
    
    

# # Exercise 3 — Sum of a List

# numbers = [10, 20, 30, 40, 50]

# total = 0


# for num in numbers:
    
#     total += num
    
# print(f"Sum Of List: {total}")



# # Exercise 4 — Count Even Numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# count = 0

# for i in numbers:
    
#     if i % 2 ==  0:
        
#         count += 1
        

# print(f"Total Even Numbers: {count}")



# Exercise 5 একটি list থেকে সবচেয়ে বড় সংখ্যা খুঁজে বের করো।

numbers = [12, 45, 7, 89, 23]

max_num = numbers[0]

for num in numbers:
    
    if num > max_num:
        
        max_num = num
        
print(f"Max Number in List: {max_num}")


# Exercise 6 — Function দিয়ে Largest Number বের করো

def find_largest(numbers):
    
    max_val = numbers[0]
    
    for num in numbers:
        
        if num > max_val:
            
            max_val = num
            
    return max_val

numbers = [12, 45, 7, 89, 23]

result = find_largest(numbers)

print(result)



# Exercise 7 — Find Smallest Number


def find_smallest(numbers):
    
    min_val = numbers[0]
    
    for num in numbers:
        
        if num < min_val:
            
            min_val = num
            
    return min_val

numbers = [12, 45, 7, 89, 23]

result = find_smallest(numbers)

print(result)


#  Exercise 8 — দ্বিতীয় বৃহত্তম সংখ্যা বের করো


def find_second_largest(numbers):
    
    n = len(numbers)
    
    for i in range(n - 1):
        
        for j in range(n - i - 1):
            
            if numbers[j] < numbers[j +1]:
                
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return numbers[1]        
            

numbers = [12, 45, 7, 89, 23]

print(find_second_largest(numbers))



# Exercise 9 — Function দিয়ে দ্বিতীয় বৃহত্তম সংখ্যা বের করো

def find_second_largest(numbers):
    
    second_largest = numbers[0]
    
    largest = numbers[0]
    
    for num in numbers:
        
        if num > largest:
            
            second_largest = largest
            
            largest = num
            
        elif num > second_largest and num < largest:
            
            second_largest = num
            
        
    
    return second_largest
    
    
numbers = [12, 45, 7, 89, 23]

print(find_second_largest(numbers))


# Exercise 10 — দ্বিতীয় ক্ষুদ্রতম সংখ্যা

def find_second_smallest(numbers):
    
    smallest = numbers[0]
    
    second_smallest = float('inf')
    
    for num in numbers:
        
        if num < smallest:
            
            second_smallest = smallest
            
            smallest = num
            
        
        elif num > smallest and num < second_smallest:
            
            second_smallest = smallest
            
            
    return second_smallest


numbers = [15, 8, 25, 3, 12]

print(find_second_smallest(numbers))



# Exercise 11 একটি লিস্টে কতগুলো জোড় সংখ্যা আছে

def count_even(numbers):
    
    count = 0
    
    for num in numbers:
        
        if num % 2 == 0:
            
            count += 1
    
    return count


numbers = [2, 5, 8, 11, 14, 17]

print(count_even(numbers))


# Exercise 12 — জোড় সংখ্যার যোগফল

def sum_even(numbers):
    
    total = 0
    
    for num in numbers:
        
        if num % 2 == 0:
        
            total +=  num
            
    return total
    
numbers = [2, 5, 8, 11, 14, 17]

print(sum_even(numbers))


# Exercise 13 — Function দিয়ে জোড় ও বিজোড় সংখ্যা আলাদা


def get_even_numbers(numbers):
    
    new_list = []
    
    for num in numbers:
        
        if num % 2 == 0:
            
            new_list.append(num)
            
    return new_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(get_even_numbers(numbers))


# Exercise 14 — বিজোড় সংখ্যাগুলো বের করো

def get_odd_numbers(numbers):
    
    new_list = []
    
    for num in numbers:
        
        if num % 2 == 1:
            
            new_list.append(num)
            
    return new_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(get_odd_numbers(numbers))


# Exercise 15 — Function দিয়ে সংখ্যার সংখ্যা গণনা

def count_number(numbers, target):
    
    count = 0
    
    for num in numbers:
        
        if num == target:
            
            count += 1
    
    return count

numbers = [2, 5, 2, 8, 2, 9, 5]

print(count_number(numbers, 2))


# Exercise 16 — Function দিয়ে একটি সংখ্যা প্রাইম কি না পরীক্ষা করো


def is_prime(n):
    
    if n < 2:
        
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        
        if n % i == 0:
            
            return False
            
    return True


print(is_prime(7))   # True
print(is_prime(10))  # False


# Exercise 17 — একটি লিস্ট থেকে Prime Number বের করো

def get_primes(numbers):
    
    new_list = []
    
    for num in numbers:
        
        if is_prime(num):
            
            new_list.append(num)
            
    return new_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(get_primes(numbers))


# Exercise 18 — লিস্টের সব সংখ্যার Factorial বের করো

def factorial(n):
    
    facto = 1
    
    for i in range(1, n + 1):
        
        facto *= i
    
    return facto

print(factorial(5))  # 120
print(factorial(4))  # 24


# Task: n = 5832 হলে এক এক করে সব digit বের করবে।

def find_digit(n):
    
    n = abs(n)
    
    while n > 0:
        
        digit = n % 10
        
        print(digit, end=' ')

        
        n = n //10
        
    print()     

n = 5832

find_digit(n)


# sum_digit(n) — digit-গুলোর যোগফল বের করা।

def sum_digit(n):
    
    n = abs(n)
    
    total = 0 
           
    while n > 0:
            
        digit = n % 10
            
        total += digit
            
        n = n //10
        
    return total
        

n = 5832

print(sum_digit(n))


# count_digit(n) — মোট digit গোনা।


def count_digit(n):
    
    n = abs(n)
    
    count = 0
    
    while n > 0:
        
        count += 1
        
        n = n // 10
        
    return count


n = 1020503102

print(count_digit(n))


# Number reverse করো

def reverse_digit(n):
    
    n = abs(n)
    
    rev = 0
    
    while n > 0:
        
        digit = n % 10
        
        rev = rev * 10 + digit
        
        n = n // 10
        
    return rev


n = 1020503102

print(reverse_digit(n))


# Task 5: একটি function লেখো, যেটা সংখ্যার digit-গুলোর মধ্যে সবচেয়ে বড় digit বের করবে।

def find_large_digit(n):
    
    n = abs(n)
    
    large_digit = 0
    
    while n > 0:
        
        digit = n % 10
        
        if digit > large_digit:
            
            large_digit = digit
        
        n = n // 10
        
    return large_digit


n = 1020503102

print(find_large_digit(n))


# Task 6 — সবচেয়ে ছোট digit বের করো

def find_smallest_digit(n):
    
    n = abs(n)
    
    smallest_digit = float('inf')
    
    while n > 0:
        
        digit = n % 10
        
        if digit < smallest_digit:
            
            smallest_digit = digit
            
        n = n // 10
        
    return smallest_digit

print(find_smallest_digit(583274))

print(find_smallest_digit(583274))


# একটি function লেখো, যেটা সংখ্যায় কতবার 0 আছে তা গুনবে।


def count_zero(n):
    
    n = abs(n)
    
    count = 0
    
    while n > 0:
        
        digit = n % 10
        
        if digit == 0:
            
            count += 1
        
        n = n // 10
        
    return count


n = 1020503102

print(count_zero(n))


# এমন একটি function লেখো, যেটা একটি সংখ্যার জোড় digit-এর সংখ্যা গুনবে।


def count_even_digit(n):
    
    n = abs(n)
    
    count = 0
    
    while n > 0:
        
        digit = n % 10
        
        if digit % 2 == 0:
            
            count += 1
        
        n = n // 10
        
    return count


n = 58327460

print(count_even_digit(n))


# একটি function লেখো count_digit(n), যেটা সংখ্যাটিতে মোট কয়টি digit আছে তা return করবে।

def count_digit(n):
    
    n = abs(n)
    
    count = 0
    
    
    while n > 0:
        
        count +=1
        
        n = n // 10
        
    return count

print(count_digit(58329))



# Intermediate Challenge 1: Second Largest Unique Number


def second_largest(numbers):
    
    large_number = None
    
    second_largest = None
    
    
    for num in numbers:
        
        if large_number is None or num > large_number:
            
            if num != large_number:
            
                second_largest = large_number
            
                large_number = num
            
        elif num != large_number and (second_largest is None or num > second_largest):
            
            second_largest = num
            
    return second_largest


print(second_largest([10, 5, 8, 20, 15]))

print(second_largest([4, 4, 9, 9, 7]))

print(second_largest([5, 5, 5]))

print(second_largest([5, 5, 4]))


# Intermediate Challenge 2 — Consecutive Duplicates Remove

def remove_duplicates(numbers):
    
    new_list = []
    
    for num in numbers:
        
        if num not in new_list:
            
            new_list.append(num)
    
    return new_list


print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))


#  Intermediate Challenge 3 — Find the First Non-Repeating Character

def first_unique_char(text):
    
    freq =  {}
    
    for char in text:
        
        if char not in freq:
            
            freq[char] = 1
        else:
            
            freq[char] += 1
    
    
    for x, y in freq.items():
        
        if y == 1:
            
            return x
            

print(first_unique_char("aabbcdd"))  # c
print(first_unique_char("swiss"))   # w
print(first_unique_char("aabb"))    # None


# Intermediate Challenge 4 — Group Anagrams

def group_anagrams(words):
    
    groups = {}
    
    for word in words:
        
        key = "".join(sorted(word))
        
        if key not in groups:
            
            groups[key] = []
            
        groups[key].append(word)
        
    return list(groups.values())



words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))

''' Python function practice continue koro. Ami Intermediate Challenge 4 — Group Anagrams porjonto sesh korechi. 
Ekhane theke porer challenge dao, ar Banglay step-by-step bujhao.'''
