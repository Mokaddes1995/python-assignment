#Create List

fruits = ["Apple", "Banana", "Orange", "Mango"]
print(fruits)

#Access Item

fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[1]) # Return Banana
print(fruits[2]) # Return Orange
print(fruits[3]) # Return Mango

#List Indexing

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(len(thislist))

#Negative Indexing

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-1]) # Return mango

print(thislist[-5]) # Return cherry

#Slicing List

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:7]) #Return cherry", "orange", "kiwi", "melon

print(thislist[-7:-1]) #Return "apple", "banana", "cherry", "orange", "kiwi", "melon"

print(thislist[-1:-7:-1]) # Return 'mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana'

print(thislist[-1:-7]) # Return Empty List

print(thislist[5:-1]) # Return "melon"

#Check Item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

a =  "Yes" if "apple" in thislist else "No" # Return Yes; This Called Ternary Operator

print(a)

if "banana" in thislist:
    print('Yes, banana  in thislist.') # Return Yes, banana  in thislist.


if 'banana' not in thislist:
    print("No, banana not in thislist.")
else:
    print("Yes, banana in thislist.") # Return Yes, banana  in thislist.
    

if 'Egg' in thislist:
    print("Yes, Egg in thislist.")
else:
    print("No, Egg not in thislist.") # Return "No, Egg not in thislist."
    

#Change Item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)

thislist[4] = ["Guava"]

print(thislist) # Return ["apple", "banana", "cherry", "orange", "Guava", "melon", "mango"]

thislist[0] = ["malta"]

print(thislist) # Return ['malta', 'banana', 'cherry', 'orange', 'Guava', 'melon', 'mango']

#Change Item in Range

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)

thislist[1:3] = ["guava", "malta"]

print(thislist) # Return ['apple', 'guava', 'malta', 'orange', 'kiwi', 'melon', 'mango']

""" Change Item in Range এর ক্ষেত্রে কম আইটেম যদি দেওয়া হয় তাহলে যে কয়টি আইটেম দেওয়া হয়েছে সেগুলো থাকবে
বাকিগুলো Range এর বাইরের গুলো রিমুভ হয়ে যাবে এবং লিস্ট এর আকার কমে আসবে। আর যদি বেশী দেওয়া হয় তাহলে সেটি Range এ যোগ হবে এবং
লিস্টের আকার বড় হবে। """

thislist = ["orange", "kiwi", "melon", "mango"]

thislist[1:3] = ["apple"]

print(thislist) # Return ['orange', 'apple', 'mango'] ; melon are removed and list length 3

thislist = ["orange", "kiwi", "melon", "mango"]

thislist[1:3] = ['orange', 'apple', 'mango'] # Return ['orange', 'orange', 'apple', 'mango', 'mango']

print(thislist)

#Insert Items Using insert() method

mylist = [1,2,3,4,5,6]

print(mylist) # Return [1,2,3,4,5,6]

# insert() এর ক্ষেত্রে ইনডেক্সে যেটা insert করতে চাই সেটা যোগ হবে এবং বাকি আইটেমগুলোও থাকবে পরিবর্তিত হবে না। শুধুমাত্র ইনডেক্স নম্বর পরিবর্তন হবে।

mylist.insert(0, "Apple")

print(mylist) # Return ['Apple', 1, 2, 3, 4, 5, 6]

mylist.insert( 1, "Orange")

print(mylist) # Return ['Apple', 'Orange', 1, 2, 3, 4, 5, 6]


#Append List 

thislist = ['orange', 'apple', 'cherry', 'mango', 'melon']

thislist.append("kiwi") # Add in last

print(thislist) # Return ['orange', 'apple', 'cherry', 'mango', 'melon', 'kiwi']

thislist.append(2)

print(thislist)

#Extend list

thislist = ['orange', 'apple', 'cherry', 'mango', 'melon']

mylist = [1, 2, 3, "banana"]

thislist.extend(mylist)

print(thislist)

# Tuple, Set, Dictionary সমূহ extend method use করে বড় করা যায়। এবং সব গুলো শেষ থেকে যোগ হয়।

thislist = ['orange', 'apple', 'cherry', 'mango', 'melon']

mytuple = ("ant", "life", "mio")

thislist.extend(mytuple)

print(thislist)


#Remove Item

thislist = ['orange', 'apple', 'cherry', 'mango', 'melon']

# Specific Item Remove করতে remove() method ব্যবহার করা হয়।

thislist.remove("apple")

print(thislist) # Remove 'apple'

thislist.remove("melon")

print(thislist) # Remove 'melon'

# Specific Index Remove করতে pop() method ব্যবহার করা হয়।

thislist = ['orange', 'apple', 'cherry', 'mango', 'melon']

thislist.pop(2)

print(thislist) # pop 'cherry'

thislist.pop(2)

print(thislist) # pop 'mango'

# pop(খালি রাখলে শেষের আইটেমটি রিমুভ হবে)

thislist = ['orange', 'apple', 'cherry', 'mango', 'melon']

thislist.pop()

print(thislist) # pop "melon"


#Use del

x = ['orange', 'apple', 'cherry', 'mango', 'melon']

# del ব্যবহার করে লিস্টটিকে ডিলিট করা হয়

del x

#Use clear

x = ['orange', 'apple', 'cherry', 'mango', 'melon']

# clear ব্যবহার করলে লিস্টটির আইটেমসমূহ থাকেবে না কিন্তু খালি লিস্ট থাকবে।

x.clear()

print(x) # Return x = []

# Loop List

#While Loop

x = ['orange', 'apple', 'cherry', 'mango', 'melon']

i = 0

while i < len(x):
          
    print(f"{i+1}: {x[i]}")
    
    i += 1

#For Loop

x = ['orange', 'apple', 'cherry', 'mango', 'melon']

for i, fruit in enumerate(x):
    print(f"{i+1}. {x[i]}")
    

for fruit in x:
    print(fruit)
    
for i in range(len(x)):
    print(f"{i+1}: {x[i]}")
    
    
    
    


