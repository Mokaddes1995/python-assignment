# # Task 1: Create a Dictionary

# # Create a dictionary of a person with name, age, and city

# # Expected: {"name": "Alice", "age": 25, "city": "NYC"}

# person = {
#     "name" : "Alice",
#     "age" : 25,
#     "city" : "NYC"
# }

# print(person)

# #Task 2: Access Values

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Print the person's name and age

# print(person["name"])

# print(person["age"])


# # Task 3: Add New Key-Value Pair

# person = {"name": "Alice", "age": 25}

# # Add "city": "NYC" to the dictionary

# print(person)

# person["city"] = "NYC"

# print(person)

# # Task 4: Update Existing Value

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Change age to 26

# person["age"] = 26

# person.update({"age" : 26})

# print(person)

# # Task 5: Delete a Key

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Delete "city" from the dictionary

# person.pop("city")

# print(person)

# # Task 6: Check if Key Exists

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Check if "age" exists in the dictionary

# if "age" in person:
#     print("Yes")
# else:
#     print("No")

# # Task 7: Get All Keys

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Print all keys

# x = person.keys()

# print(x)

# # Task 8: Get All Values

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Print all values

# y = person.values()

# print(y)

# # Task 9: Get All Items (Key-Value Pairs)

# person = {"name": "Alice", "age": 25, "city": "NYC"}

# # Print all key-value pairs

# x = person.items()

# print(x)


# # Task 10: Get Value with Default

# person = {"name": "Alice", "age": 25}

# # Try to get "city" with a default value "Unknown"

# x = person.setdefault("city", "Unknown")

# print(person)


# #Nested Dictionary

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# #Access Child Name & Year

# #Child 3 Name

# print("*" * 10)

# print(f" Child 3 Name : {myfamily["child3"]["name"]} and Age: {myfamily["child3"]["year"]}")




# for child, value in myfamily.items():
#     print()
#     print(child)
#     print("*" * 10)
    
#     for key, value in value.items():
#         print(key, ": ", value)
        

# # Input Dictionary

# if __name__ == '__main__':
    
#     students = {}
    
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
#         students[name] = score
        
# print(students)


# Nested Dictionary


if __name__ == '__main__':
  
  my_dict = {}
  
  for _ in range(int(input())):
    
    key = input("Main Key: ")
        
    sub_dict = {}
    
    for  _ in range(int(input("How many Sub_dict: "))):
      
      s_key = input()
      s_value = input()
      
      if s_key == "age":
        s_value = int(s_value)
    
      sub_dict[s_key] = s_value
    
    my_dict[key] = sub_dict
  
print(my_dict)