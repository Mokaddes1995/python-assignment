# Selection Sort

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n -1):
    
    min_index = i
    
    for j in range(i + 1, n):
        
        if my_array[j] < my_array[min_index]:
            
            min_index = j
            
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
    
    
print(f"Sorted Arrays: {my_array}")



my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n -1):
    
    min_index = i
    
    for j in range(i + 1, n):
        
        if my_array[j] > my_array[min_index]:
            
            min_index = j
            
    my_array[min_index], my_array[i] = my_array[i], my_array[min_index]

    
    
print(f"Sorted Arrays: {my_array}")     


# Problem 1: Basic Selection Sort  


arr = [29, 10, 14, 37, 13]

n = len(arr)

for i in range(n - 1):
    
    min_index = i
    
    for j in range(i + 1, n):
        
        if arr[j] < arr[min_index]:
            
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]
    

print(f"Ascending from Minimum Value:{arr}")


# Problem 2: Find Minimum

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n - 1):
    
    min_index = i
    
    for j in range(i + 1, n):
        
        if arr[j] < arr[min_index]:
            
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]
    

print(f"Sorted By using Selection Sort: {arr}")


# Problem 3: Count Passes

arr = [7, 4, 9, 2, 6]

n = len(arr)

count = 0

for i in range(n - 1):
    
    min_index = i
    
    for j in range(i + 1, n):
        
        if arr[j] < arr[min_index]:
            
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
    count += 1
    

print(f"Sorted Array: {arr}")

print(f"Count: {count}")


# Problem 4: Duplicate Values

arr = [3, 3, 1, 2, 1]

n = len(arr)

for i in range(n - 1):
    
    min_index =  i
    
    for j in range(i + 1, n):
        
        if arr[j] < arr[min_index]:
            
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]
    

print(f"Sorted With Duplicate: {arr}")

# Problem 5: Larger Array

arr = [20, 5, 17, 8, 1, 12]

n = len(arr)


for i in range(n - 1):
    
    min_index = i
    
    for j in range(i + 1, n):
        
        if arr[j] < arr[min_index]:
            
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"Pass No {i + 1}: {arr}")
    
print(f"Sorted Array: {arr}")