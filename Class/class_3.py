
#Multiplication of 6

for i in range(1,11):
    if i % 2 == 1:
        continue
        
    print(f"6 x {i} = {6 * i}")

#Swapcase

my_input = "Enter Your Input:"

result = ''

for i in my_input:
    if "A" <= i <="Z":
       result += i.lower()
    elif 'a' <= i <= 'z':
        result += i.upper()
    else:
        result += i
        
print(result)
print(result[::-1])

print(ord("A"))


#Chain Comparison

my_input = int(input("Enter Your Age: "))

if 0 <= my_input <= 12:
    print("0-12: Child")
elif 13 <= my_input <= 19:
    print("13-19: Teenager")
elif 20 <= my_input <=  59:
    print("20-59: Adult")
elif my_input >= 60:
    print("60+: Senior")
else:
    print("Invalid Syntex")


char = input("Enter you Char: ")

if "A" <= char <= "Z":
    print("A-Z: Uppercase")
elif "a" <= char <= "z":
    print("a-z: Lowercase")
elif "0" <= char <= "9":
    print("0-9: Digit")
else:
    print("Special Charecter")
    
    
my_input = input("Enter you Char: ")

for char in my_input:

    if "A" <= char <= "Z":
        print(f"{char}: Uppercase")
    elif "a" <= char <= "z":
        print(f"{char}: Lowercase")
    elif "0" <= char <= "9":
        print(f"{char}: Digit")
    else:
        print("Special Character")

