#Create Tuple

mytuple = ('Apple', 'Orange', "Banana", "Mango")

print(mytuple)

# Access the 3rd element of a tuple (10, 20, 30, 40, 50).

my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[2])

# Slice a tuple to get elements from index 1 to 4.

my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[1:4])

# Concatenate two tuples: (1, 2, 3) and (4, 5, 6).

tuples_1 = (1, 2, 3)

tuples_2 = (4, 5, 6)

tuple_3 = tuples_1 + tuples_2

print(tuple_3)

# Repeat a tuple ("Hi",) 5 times using the * operator.

this_list = ("Hi",)

my_list = this_list * 5

print(my_list)

# Check if 50 exists in the tuple (10, 20, 30, 40, 50).

my_tuple = (10, 20, 30, 40, 50)

res = "Yes, 50 in my_tuple" if 50 in my_tuple else "No 50 not in my_tuple"
print(res)


#Find the length of a tuple without using len() (use a loop).

my_tuple = (10, 20, 30, 40, 50)

length = 0

for i, num in enumerate(my_tuple):
    
    length += 1
   
print(length)

# Convert a list [1, 2, 3, 4] into a tuple.

_list = [1, 2, 3, 4]

_tuple = tuple(_list)
print(_tuple)

# Convert a tuple ("a", "b", "c") into a list.

tuple_6 = ("a", "b", "c")

list_1 = list(tuple_6)

print(list_1)

#Unpack a tuple (name, age, city) = ("Alice", 25, "NYC") and print each.



