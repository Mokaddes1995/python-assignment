import math

# # Problem 2: Sum of 1 to N (Loop)

# # User থেকে N নিন

# number = int(input("NUmber: "))

# # 1 থেকে N পর্যন্ত সব সংখ্যার যোগফল প্রিন্ট করুন

# # Use For Loop

# total = 0

# for num in range(1, number + 1):
    
#     total += num

# print(f"Total = {total}")


# # While Loop

# i = 0

# total = 0

# while i <= number:
    
#     total += i
    
#     i +=1
    
# print(f"Total: {total}")
    
# # Input: 5
# # Output: 15  (1+2+3+4+5)


# # Problem 3: Count Vowels (String)

# # User থেকে একটি string নিন

# n = input('Enter Word: ')

# # কতগুলো vowel (a, e, i, o, u) আছে তা প্রিন্ট করুন

# vowels = 'aeiouAEIOU'

# count = 0

# for char in n:
    
#     if char in vowels:
#         count += 1  

# print(count)

# # Input: hello world
# # Output: 3


# # Problem 4: Find Max in List (List)

# n = list(map(int, input('Create list: ')))

# # একটি list থেকে সবচেয়ে বড় সংখ্যা বের করুন

# # max() ব্যবহার করবেন না

# max_number = n[0]

# for num in n:
    
#     if max_number < num:
        
#         max_number = num

# print(f"Max Number Of List: {max_number}")

# # Input: [3, 7, 2, 9, 4]
# # Output: 9


# # Problem 5: Reverse String (Slicing)

# # User থেকে একটি string নিন

# input_string = input('Enter String: ')

# # String টি উল্টো করে প্রিন্ট করুন

# reverse_string = input_string[::-1]

# print(reverse_string)

# # Input: Python
# # Output: nohtyP

# # Problem 6 — Palindrome Checker

# if input_string == reverse_string:
#     print("Palindrome")
# else:
#     print('Not Palindrome')

# # Problem 7: Count Frequency (Dictionary)

# # একটি string এ প্রতিটি character কতবার আছে তা count করুন

# input_string = input('Enter String: ')

# # Dictionary তে সংরক্ষণ করুন

# char_count = {}

# # for char in input_string:
    
# #     count = input_string.count(char)
    
# #     char_count[char] = count

# # print(char_count)   


# # for char in input_string:
    
# #     char_count[char] = input_string.count(char)

# # print(char_count)


# for char in input_string:
    
#     if char in char_count:
        
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
       
# print(char_count)
    

# # Input: hello
# # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# # Word counter

# string = input().split(' ')

# my_dict = {}


# for word in string:
    
#     if word in my_dict:
#         my_dict[word] += 1
#     else:
#         my_dict[word] = 1
        
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

    
# # Problem 7: Check Prime (Function) 

# def is_prime(num):
    
#     if num < 2:
        
#         return False
        
#     for i in range(2, int(num ** 0.5) + 1):
        
#         if num % i == 0:
            
#             return False
            
#     return True


# print(is_prime(2))


    



    
    