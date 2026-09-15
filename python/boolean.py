# Challenge 1

is_raining = True

if is_raining:
    print("It is Raining")
else:
    print("No Rain")
    

# Challenge 2

is_hungry = False

if is_hungry:
    print("I am Hungry")
else:
    print("I am Not Hungry")
    

# Challenge 3 — একটু কঠিন

is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Welcome Admin")
elif is_logged_in and not is_admin:
    print("Welcome User")
else:
    print("Please Login")
    

# Challenge 4 — 🔥 তোমার Car

is_start = False
speed = 0

#start()

if is_start:
    print('Car Already Start')
else:
    is_start = True
    print('Car Started')

#accelerate()

if is_start:
    speed += 10
    print(f'Your Car Speed is {speed} km/h')
else:
    print('Start Car First')

#brake()

if is_start:
    
    speed -= 5
    
    if speed < 0:
        speed = 0
    
    print(f"Speed: {speed}")
else:
    print("Start Car First")
    

    
    
is_start = False


'''
যদি গাড়ি আগে থেকেই চালু থাকে (True) → "Car Already Started" print করবে।
যদি গাড়ি বন্ধ থাকে (False) → গাড়িটাকে চালু করবে এবং "Car Started" print করবে।
শেষে is_start-এর value print করবে।'''

if is_start:
    print('Car Already Started')
else:
    is_start = True
    print('Car Started')

print(is_start)


is_start = False

'''
is_start == True হলে → "Car Stopped" print হবে এবং is_start = False হবে।
is_start == False হলে → "Car Already Stopped" print হবে।
শেষে is_start print করবে।'''

if is_start:
    
    is_start =False
    
    print('Car Stopped')
else:
    
    print('Car Alreay Stopped')

print(is_start)


is_start = False


if is_start:
    print('Car Stopped')
else:
    is_start = True
    print('Car Started')
    

if is_start:
    is_start = False
    print('Car Stopped')
else:
    print('Car Already Stopped')
    

print(is_start)


# Task 1 — Light 💡

is_on = False


if is_on:
    print('Light Already ON')
else:
    is_on = True
    print('Light is ON')
    

print(is_on)

# Task 2 — Door 🚪

is_open = True


if is_open:
    is_open = False
    print("Door Closed")
else:
    print('Door Already Closed')
    
print(is_open)


# Task 3 — Fan 🌀

is_running = True


if is_running:
    print("Fan Already Running")
else:
    is_running = True
    print('Fan Started')
    
if is_running:
    is_running = False
    print('Fan Stopped')
else:
    print('Fan Already Stopped')

print(is_running)


#  Task 4 — Login 🔐

is_logged_in = False


if not is_logged_in:
    is_logged_in = True
    print("User Logged In")


if is_logged_in:
    print("Already Logged In")  


print(is_logged_in)


# Task 5 — ATM Card 💳

has_card = True

if has_card:
    has_card = False
    print("Card Removed")
else:
    
    print('Card Already Removed')


if not has_card:
    print("Please Insert Card")   
else:
    print("Card Already Inserted")

print(has_card)


