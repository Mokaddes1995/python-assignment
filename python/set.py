# #Create a Set

# my_set = {"apple", "banana", "cherry", "mango", "apple", "banana"}

# print(my_set)

# #Access Item 

# my_set = {"apple", "banana", "cherry", "mango"}

# for i in my_set:
#     print(i)
    

# #Add Items

# blank_set = {"Apple", "Banana"}

# blank_set.add("Mango")

# print(blank_set)

# for i in my_set:
#     blank_set.add(i)
    
# print(blank_set)

# #Add Set

# my_set = {1, 2, 3, 4, 5}

# blank_set = {6, 7, 8}

# blank_set.update(my_set)

# print(blank_set)

# #Add Any Iterable Item

# this_set = {"Mahir", "Raiyan"}
# this_list = ["Mokaddes", "Rabeya"]

# this_set.update(this_list)

# print(this_set)

# #Remove Items

# my_set = {"apple", "banana", "cherry", "mango"}

# my_set.remove("apple")

# print(my_set)

# # my_set.remove("apple") #raise error

# #Use discard()

# my_set.discard("apple")
# print(my_set) #Not raise Error

# #Use pop() for random value Remove

# my_set.pop()
# print(my_set) #Not sure what item are removed


# # Use clear() for Empty Set

# my_set = {"apple", "banana", "cherry", "mango"}

# my_set.clear()

# print(my_set) #Empty Set

# #Use del for delete set

# del_set = {"apple", "banana", "cherry", "mango"}

# del del_set

# #print(del_set) #Raise Error


# # Loop 

# loop_set = {"Apple", "Mokaddes", "Sohan", "Cherry"}

# for x in loop_set:
#     print(x)
    

# # Join Set By Union

# even_numbers = {2, 4, 6, 8, 10}
# odd_numbers = {1, 3, 5, 7, 9}

# myset_2 = even_numbers.union(odd_numbers)

# print(myset_2)

# # Alternative Option

# myset_3 = even_numbers| odd_numbers

# print(myset_3)

# # Join 4 Set

# even_numbers = {2, 4, 6, 8, 10}
# odd_numbers = {1, 3, 5, 7, 9}
# vowels = {'a', 'e', 'i', 'o', 'u'}
# colors = {'red', 'blue', 'green', 'yellow'}

# myset_4 = even_numbers.union(odd_numbers, vowels, colors)

# print(myset_4)


# # Alternative

# myset_5 = even_numbers|odd_numbers|vowels|colors

# print(myset_5)


# #Join a Set and Tuple

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)

# print(z)

# # Alternative

# #z = x | y

# #print(z) #Raise Error


# #Use Intersection

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# C = A.intersection(B)

# print(C)

# #Alternative

# D = A & B

# print(D)

# Create a set of 5 favorite colors and print it.

colors = {"Red", "Green", "Blue", "White", "Magenta"}

print(colors)

# Add the color "Purple" to an existing set {"Red", "Blue", "Green"}

colors = {"Red", "Blue", "Green"}

colors.add("Purple")

print(colors)

# Remove "Blue" from the set using remove() and discard() (show both).

colors = {"Red", "Blue", "Green"}

colors.remove("Blue")

print(colors)

colors.discard("Blue")

print(colors)

# Check if "Yellow" exists in the set {"Red", "Blue", "Green"}.

colors = {"Red", "Blue", "Green"}

print("Yellow" in colors)

# Find the length of a set without using len() (use a loop).

colors = {"Red", "Green", "Blue", "White", "Magenta"}

length = 0

for i in colors:
    length  +=1

print(length)

# Convert a list [1, 2, 2, 3, 4, 4, 5] into a set to remove duplicates.

my_list = [1, 2, 2, 3, 4, 4, 5]

#Convert to Set

my_set = set(my_list)

print(my_set)

# Convert a set {1, 2, 3} back into a list.

new_set = {1, 2, 3}

# Convert Set to List

new_list = list(new_set)

print(new_list)

# Loop through a set and print each element.

colors = {"Red", "Green", "Blue", "White", "Magenta"}

for i in colors:
    print(i)

# Clear all elements from a set using clear().

colors = {"Red", "Green", "Blue", "White", "Magenta"}

colors.clear()

print(colors)

# Create an empty set (not a dictionary!) and add 3 items to it.

fruits = set()

fruits.add("apple")
fruits.add("orange")
fruits.add("cherry")

print(fruits)

# Intermediate

# Find the union of two sets: {1, 2, 3} and {3, 4, 5}.

set_1 = {1, 2, 3}

set_2 = {3, 4, 5}

union_set = set_1.union(set_2)

print(union_set)

# Alternative Way

union_set = set_1 | set_2

print(union_set)

# Find the intersection of two sets: {1, 2, 3, 4} and {3, 4, 5, 6}.

set_3 = {1, 2, 3, 4}

set_4 = {3, 4, 5, 6}

intersection_set =  set_3.intersection(set_4)

print(intersection_set)

#Alternative Way

intersection_set = set_3 & set_4

print(intersection_set)

# Find the difference between two sets: {1, 2, 3, 4} and {3, 4, 5, 6}.

set_3 = {1, 2, 3, 4}

set_4 = {3, 4, 5, 6}

difference_set = set_3.difference(set_4)

print(difference_set)

#Alternative Way

difference_set = set_3 - set_4

print(difference_set)


# Find the symmetric difference of {1, 2, 3} and {1, 2, 3}.

set_5 = {1, 2, 3}

set_6 = {1, 2, 3}

symmetric = set_5.symmetric_difference(set_6)

print(symmetric)

# Check if set A {1, 2} is a subset of set B {1, 2, 3, 4}.

A = {1, 2}

B = {1, 2, 3, 4}

if A.issubset(B):
    
    print("Yes, Set A is subset of Set B")
else:
    print("No, Set A is subset of Set B")


# Check if set A {1, 2, 3, 4} is a superset of set B {2, 3}.

A = {1, 2, 3, 4}

B = {2, 3}

if A.issuperset(B):

    print("Yes, Set A superset Of Set B")
else:
    print("NO, Set A superset Of Set B")


# Check if two sets are disjoint: {1, 2, 3} and {4, 5, 6}.

x = {1, 2, 3}

y = {4, 5, 6}

z = x.isdisjoint(y)

print(z)

# Remove duplicates from a list [1, 2, 2, 3, 3, 3, 4] while keeping order (use set + list).

duplicate_list = [1, 2, 2, 3, 3, 3, 4]

remove_duplicates = list(set(duplicate_list))

print(remove_duplicates)

# Find common elements between 3 sets: {1,2,3}, {2,3,4}, {3,4,5}.

a = {1,2,3}

b = {2,3,4}

c = {3,4,5}

common_item = a & b & c

print(common_item)

# Update a set with elements from another set using update().

a = {1,2,3}

b = {4,5,6}

a.update(b)

print(a)

# Use set comprehension to create a set of squares for numbers 1-10.

squares = {x ** 2 for x in range(1, 11)}

print(squares)

# Use set comprehension to create a set of even numbers from 1-20

even_nums = {x for x in range(1, 20) if x % 2 == 0}

print(even_nums)

# Find unique characters in a string "hello world" using a set.

string = "hello world"

unique_char = set(string.replace(" ", ""))

print(unique_char)

# Count unique vowels in a sentence "The quick brown fox jumps over the lazy dog"

sentence = "The quick brown fox jumps over the lazy dog"

vowels = 'aeiou'

vowels_set = ""

for x in sentence.replace(" ", ""):
    for j in vowels:
        if x == j:
            vowels_set += x
    

print(len(set(vowels_set)))  

# Find the symmetric difference of 3 sets: {1,2,3}, {2,3,4}, {3,4,5}.

a = {1,2,3}

b = {2,3,4}

c = {3,4,5}

symmetric_diff = a ^ b ^ c

print(symmetric_diff)

# Remove elements from a set that are present in another set (using difference_update()).

a = {1,2,3}

b = {2,3,4}

a.difference_update(b)

print(a)

# Keep only elements from set A that are also in set B (using intersection_update()).

A = {1,2,3}

B = {2,3,4}

A.intersection_update(B)

print(A)


# Compare two sets and return elements that are in first but not in second, and vice versa. 

A = {1,2,3}

B = {2,3,4} 

elements = A.difference(B)

elements_2 = B.difference(A)

print(elements)

print(elements_2)


# Task 31: Find mutual friends

alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Charlie", "Eve", "Frank", "Grace"}

# Find friends common to both

common_friend = alice_friends & bob_friends

print(f"Common Friend: {common_friend}")

# Find friends only Alice has

Alice_has = alice_friends.difference(bob_friends)

print(f"Alice Has : {Alice_has}")

# Find friends only Bob has

bob_has = bob_friends.difference(alice_friends)

print(f"Bob Has : {bob_has}")

# Task 32: Tag system

post1_tags = {"python", "coding", "tutorial"}
post2_tags = {"python", "data", "science"}
post3_tags = {"coding", "fun", "projects"}

# Find tags that appear in all posts

all_post = post1_tags & post2_tags & post3_tags

print(all_post)

# Find tags that appear in at least two posts

two_post = (post1_tags & post2_tags) 

print(two_post)
# Find unique tags across all posts

# Task 33: Student enrollment

math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Charlie", "Eve", "Frank", "Grace"}
art_students = {"Alice", "Eve", "Henry"}
# Students taking both math and science
# Students taking math or art (or both)
# Students taking exactly one subject


# Given these sets:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}

# Find:
# 1. Elements in A and B but not in C
# 2. Elements in exactly two of the three sets
# 3. Elements in all three sets


