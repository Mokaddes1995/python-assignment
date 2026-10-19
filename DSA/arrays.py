# Find MinValue From a Arrays


my_arr = [7, 12, 9, 11, 3] # First Crate a Arrays

minVal = my_arr[0] #Crate a variable minVal and set it equal to first value of the arrays.

# Go to every Element by use for Loop

for i in my_arr:
    
    if i <= minVal: # if i less than of value of MinVal
        
        minVal = i # MinVal update by i.
        

print(minVal)  


# Babul Sort

arr =[7, 12, 9, 11, 3]

n = len(my_arr)

for i in range(n - 1):
    
    for j in range(n - i -1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j +1], arr[j]

print(f"Sorted Array: {arr}")


for i in range(n - 1):
    
    for j in range(n-i-1):
        
        if arr[j] < arr[j + 1]:
            
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
    
print(f'Descending Sorted: {arr}')


# Exercise 2: Find the Lowest

# Array-এর সবচেয়ে ছোট সংখ্যাটি খুঁজে বের করো।

# শর্ত: min() ব্যবহার করা যাবে না। Loop ব্যবহার করতে হবে।

arr = [15, 7, 22, 3, 10]

minVal = arr[0]

for i in arr:
    
    if i <= minVal:
        
        minVal = i

print(f"Minimum Value: {minVal}")



# Exercise 3: Find the Highest
# Array-এর সবচেয়ে বড় সংখ্যা খুঁজে বের করো।
# শর্ত: max() ব্যবহার করা যাবে না।



arr = [12, 45, 8, 67, 23]

maxVal = arr[0]

for i in arr:
    
    if i >= maxVal:
        
        maxVal = i
        
print(f"Maximum Value: {maxVal}")


# Exercise 8: Bubble Sort নিজে Implement করো

# নিচের Array-টিকে Ascending Order-এ Sort করার সম্পূর্ণ কোড লেখো।

# শর্ত:

# sort() ব্যবহার করা যাবে না।

# sorted() ব্যবহার করা যাবে না।

# Nested Loop ব্যবহার করতে হবে।


arr = [9, 4, 7, 1, 5]


n = len(arr)

for i in range(n - 1):
    
    for j in range(n - i - 1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(f"Aescending: {arr}")


# Exercise 9: Descending Order
# Bubble Sort ব্যবহার করে বড় থেকে ছোট ক্রমে সাজাও।


arr = [9, 4, 7, 1, 5]


n = len(arr)

for i in range(n - 1):
    
    for j in range(n - i - 1):
        
        if arr[j] < arr[j + 1]:
            
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

print(f"Descending: {arr}")


# Exercise 11: Improved Bubble Sort
# swapped Variable ব্যবহার করে এমন Bubble Sort লেখো, যাতে Array Sorted হয়ে গেলে আর অপ্রয়োজনীয় Pass না চলে।

arr = [1, 2, 3, 4, 5]

n = len(arr)

for i in range(n -1):
    
    swapped = False
    
    for j in range(n - i -1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] =  arr[j + 1], arr[j]
            
            swapped = True
    
    if not swapped:
        break
    
print(arr)


arr = [2, 5, 1, 4, 3]

n = len(arr)

for  i in range(n - 1):
    
    for j in range(n - i - 1):
        
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
            
print(f"Final Arr: {arr}")


# Exercise 1: Find the Minimum and Maximum
# min() ও max() ব্যবহার না করে সবচেয়ে ছোট এবং বড় সংখ্যা বের করো।

arr = [18, 5, 29, 3, 14, 40, 7]

minVal = arr[0]

maxVal = arr[0]


for i in arr:
    
    if i > maxVal:
        
        maxVal = i
    elif i < minVal:
        
        minVal = i

print(f"Maximum Value: {maxVal}")

print(f"Minimum Value: {minVal}")


# Exercise 2: Count Even and Odd
# Array-তে কয়টি Even এবং কয়টি Odd সংখ্যা আছে, তা বের করো।

arr = [2, 7, 4, 9, 12, 15, 8]

count_even = 0

count_odd = 0

for i in arr:
    
    if i % 2 == 0:
        
        count_even += 1
    else:
        
        count_odd += 1
        
print(f"Even Number: {count_even}")

print(f"Odd Number: {count_odd}")


# Exercise 3: Reverse an Array
# reverse() ব্যবহার না করে Array-টিকে উল্টো করে Print করো।

arr = [10, 20, 30, 40, 50]

new_arr =[]

for i in range(1, len(arr) + 1):
    
    new_arr.append(arr[-i])

print(new_arr)



arr = [10, 20, 30, 40, 50]

n = len(arr)

for i in range(n -1):
    
    for j in range(n - i - 1):
        
        if arr[j] < arr[j + 1]:
            
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

print(arr)   



arr = [3, 8, 12, 17, 25, 31]


n = len(arr)

for i in range(n//2):
    
    arr[i], arr[n - 1 - i] =  arr[n - 1 - i], arr[i]
    
print(arr)


