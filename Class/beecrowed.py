
# # Problem 1011: Volume Calculation

# def calculate_volume(radius):
    
#     pi = 3.14159
    
#     volume = (4/3) * pi * radius ** 3
    
#     return f"VOLUME = {volume:.3f}"


# radius = float(input())

# print(calculate_volume(radius))


# # Problem 1012: Area

# def calculate_area(a,b,c):
    
#     pi =  3.14159
    
#     triangle = 1/2 * a * c
    
#     print(f"TRINGULO: {triangle:.3f}")
    
#     circle = pi * c ** 2 
    
#     print(f"CIRCULO: {circle:.3f}")
    
#     area = 1/2 *(a + b) * c
    
#     print(f"TRAPEZIO: {area:.3f}")
    
#     area_square = b * b
    
#     print(f"QUADRADO: {area_square:.3f}")
    
#     rectangle = a * b
    
#     print(f"RETANGULO: {rectangle:.3f}")
    

# A, B, C = map(float, input().split())

# calculate_area(A, B, C)
    
    

# # Problem 1013 : Greatest

# def find_greatest(a, b, c):
    
#     if a > b and b > c:
        
#         print(f'{a} eh o maior')
        
#     elif b > a and a > c:
        
#         print(f"{b} eh o maior")
    
#     else:
#         print(f"{c} eh o maior")
    
    
    
# A, B, C = map(int, input().split())

# find_greatest(A, B, C)

# # With formula

# def find_great(a, b, c):
    
#     maior_ab = (a + b + abs(a - b)) // 2
    
#     maior = (maior_ab + c + abs(maior_ab - c)) // 2
    
#     print(f"{maior} eh o maior")
    
    
# A, B, C = map(int, input().split())

# find_great( A, B, C)


# Problem 1013: Consumption

def consumption(x, y):
    
    mileage = x / y
    
    print(f"{mileage:.3f} km/l")
    

X = int(input())

Y = float(input())

consumption(X, Y)


