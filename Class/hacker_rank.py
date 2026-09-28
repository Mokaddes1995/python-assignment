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
