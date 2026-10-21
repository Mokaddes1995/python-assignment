import json

students = {
    "name": "Mokaddes Hossain"
}

data = json.dumps(students, indent= 6)

print(data)
print(type(data))

new = json.loads(data)

print(type(new))