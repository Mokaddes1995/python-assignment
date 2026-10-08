# Fibonicci Number Use For Loop

number = int(input("Enter Number: "))

a = 0

b = 1

print(a)

print(b)


for i in range(number-2):
    
    fibo_num = b + a
    
    print(fibo_num)
    
    a, b = b , fibo_num
    
    
#Alternative

a, b = 0, 1

for i in range(number):
    
    print(a)
    
    a, b = b , a+b
    
    

# Recursive Function


x, y = 0, 1

count = 2

print(x)

print(y)


def fibonacci(x, y):
    
    global count
    
    if count <= number-1:
        
        fibonacci_num = y + x
        
        print(fibonacci_num)
        
        x, y = y, fibonacci_num
        
        count += 1
        
        fibonacci(x, y)
    else:
        return
    
fibonacci(0, 1)


# n th Fibonacci Number

def f(n):
    
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)
        

print(f(number))
    
