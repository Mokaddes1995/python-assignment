import json

import requests


# students = {
#     "name": "Mokaddes Hossain"
# }

# data = json.dumps(students, indent= 6)

# print(data)
# print(type(data))

# new = json.loads(data)

# print(type(new))


response = requests.get("https://jsonplaceholder.typicode.com/users")


data = response.json()



for i in data:
    
    print(f"\nUserId:{i['id']}")
    print(f"Name:{i['name']}")
    print(f"Email:{i['email']}\n")
   