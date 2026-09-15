# Calculate ractangle_area

def calculate_rectangle_area(l, w):
    
    area = l * w
    
    return f"Area = {area}"

height = float(input("Enter Height: "))

width = float(input('Enter width: ')) 
   
print(calculate_rectangle_area(height, width))


class Car:
    
    def __init__(self, brand, model, year):
        
        self.brand = brand
        self.model = model
        self.year = year
    
    
    def display(self):
               
        print(f"Model: {self.model}")
        
        print(f"Brand: {self.brand}")
        
        print(f"Manufacture Year : {self.year}")
        

car1 = Car("BMW", "Musting", 2000)

car1.display()