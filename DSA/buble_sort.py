# Problem 1: Basic Sorting

# Array-টিকে ছোট থেকে বড় সাজাও।

arr = [5, 3, 8, 1, 2]

# Length of Arrays

n = len(arr)

for i in range(n - 1):
    
    for j in range(n - i - 1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
    
print(f"Ascending Arrays: {arr}")


# Problem 2: Reverse Order Sorting


arr = [9, 7, 5, 3, 1]

n = len(arr)


for i in range(n - 1):
    
    for j in range(n - i -1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
    

print(f"Reverse Arrays: {arr}")


# Problem 3: Duplicate Values


arr = [4, 2, 4, 1, 3]

n = len(arr)


for i in range(n - 1):
    
    for j in range(n - i - 1):
        
        if arr[j] >= arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(f"Ascending Arrays With Duplicate Value: {arr}")


# Problem 4: Already Sorted Array


arr = [1, 2, 3, 4, 5]

n = len(arr)

for i in range(n - 1):
    
    swap = False
    
    for j in range(n - i - 1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            swap = True
            
    if not swap:
        break
    
print(f"Already Sorted Arrays: {arr}")


# Problem 5: Larger Array

arr = [12, 6, 9, 2, 15, 4]

n = len(arr)

for i in range(n - 1):
    
    for j in range(n - i - 1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
    print(f"Pass No {i + 1}: {arr}")
            

print(f"Sorted Arrays: {arr}")



# Extra Challenge

arr = [12, 6, 9, 2, 15, 4]

n = len(arr)


for i in range(n - 1):
    
    swap = False
    
    for j in range(n - i - 1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            swap = True
    
    if not swap:
        
        break
    
    print(f"Pass No {i + 1}: {arr}")
    
    
    

print(f"Array: {arr}")


# Challenge: Descending Bubble Sort

arr = [17, 3, 25, 8, 12, 1]


n = len(arr)


for i in range(n - 1):
    
    swap = False
    
    for j in range(n - i - 1):
        
        if arr[j] < arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            swap = True
            
    if not swap:
        break
    
    print(f"Pass No {i + 1}: {arr}")
    

print(f"Descending Array: {arr}")