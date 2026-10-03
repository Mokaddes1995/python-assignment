# # Hacker Rank if elif problem solved

# n = int(input().strip())
    
            
# if n % 2 == 0 and n in range(2, 6):
        
#     print("Not Weird")
                
# elif n % 2 == 0 and n in range(6, 21):
        
#     print("Weird")
    
# elif n > 20 and n % 2 == 0:
        
#         print("Not Weird")

# else:
    
#     print("Weird")

# # Decorators

# def wrapper(f):
    
#     def fun(l):
        
#         new_list = []
        
#         for number in l:
            
#             number = number[-10:]
            
#             number = "+91" + " " + number[:5] + ' ' + number [5:]
            
#             new_list.append(number)
            
#         return f(new_list)
    
#     return fun

# @wrapper
# def sort_phone(l):
    
#     print(*sorted(l), sep='\n')

# if __name__ == '__main__':
    
#     l = [input() for _ in range(int(input()))]
    
#     sort_phone(l)


# # Print hash value

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
    
#     t = tuple(integer_list)

#     print(hash(t))


# # Find a string


# def count_substring(string, sub_string):
    
#     count = 0

#     for i in range(len(string) - len(sub_string) + 1):
        
#         if sub_string == string[i:len(sub_string) + i]:
#             count += 1
            
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# # String Validators

# if __name__ == '__main__':
#     s = input()
    
#     has_alpha = False
            
#     has_alnum = False

#     has_digit = False
            
#     has_lower = False
            
#     has_upper = False


#     for i in s:
        
#         if i.isalpha():
#             has_alpha = True
            
#         if i.isalnum():
#             has_alnum = True
            
#         if i.isdigit():
#             has_digit = True
        
#         if i.islower():
#             has_lower = True
        
#         if i.isupper():
#             has_upper = True

#     print(has_alnum)
#     print(has_alpha)
#     print(has_digit)
#     print(has_lower)
#     print(has_upper)

# Pattern Matching

# s = "H"

# a = 5

# # Top Cone

# for i in range(a):
    
#     print((s * i).rjust(a - 1) + s + (s * i).ljust(a + 1))
    

# # Upper Pillar

# for i in range(a + 1):
    
#     print((s * a).center(a * 2) + (s * a).center(a * 6))
    

# # Mid

# for i in range((a + 1) // 2):
    
#     print((s * (a * a)).center(a * 6))
    

# # lower Pillar

# for i in range(a + 1):
    
#     print((s * a).center(a * 2) + (s * a).center(a * 6))
    
    
# # Bottom Cone

# for i in range(a):
    
#     print(((s * (a - i - 1)).rjust(a)+ s + (s * (a- i - 1)).ljust(a)).center(a * 6))



# Wrap Text

def wrap(string, max_width):
    
    result = ''
        
    for i in range((len(string)//max_width) + 1):
        
        result += string[i * max_width : i * max_width + max_width] + "\n"
            
    return result
       


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)