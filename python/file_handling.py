
# Create a new File 

# file = open("text.txt", 'r')

# print(file.read())

# file.close()

# f_2 = open("C://Users/monar/Desktop/NewText .txt", 'r')

# print(f_2.read())


# f_3 = open("C://Users/monar/Desktop/94th Batch/Class/text_2.txt", 'r')

# print(f_3.read(20))


# file = open("text.txt", 'r')

# print(file.readline())

# file.close()


# with open('text.txt', 'r') as my_file:
#     print(my_file.read())


# file = []


# with open('text.txt', 'r') as f:

#     for i in f:
        
#         if i.strip():
        
#             file.append(i.strip())
        
# print(file)

# new_file = [i for i in file if i != '' ]

# print(new_file)



# # Challenge: ফাইল থেকে খালি লাইন, কমেন্ট (#) এবং স্পেস লাইন বাদ কর
# # এবং লাইন নম্বর সহ প্রিন্ট কর

# file = []

# with open('text.txt', 'r') as f:
    
#     for line in f:
        
#         if line.strip() and not line.startswith('#'):
            
#             file.append(line.strip())
            

# for  i , v in enumerate(file):
#     print(f"{i+1}: {v}")
            
# print(file)

# # Expected:
# # 1: Hello World
# # 2: Python
# # 3: File


with open('text.txt', 'r') as f:
        
    content = f.readlines()
    
    print(content[0].strip())
    print(content[2])
    
    for i in content:
        print(i.strip())
    
    
