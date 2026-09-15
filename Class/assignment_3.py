# Section 1: Programming Tasks

# Task 1 (Basic Class): Create a class named Laptop with properties for brand, processor, and price. 
# Create an object of this class and print all its details.

class Laptop:
    
    # Constructor Method
    
    def __init__(self, brand, processor, price):
        self.brand = brand
        self.processor = processor
        self.price = price
        
    # Instance Method for Print Information
    
    def display_info(self):
        print()
        print("Print All Info")
        print('*' * 30)
        print(f"Brand: {self.brand}")
        print(f"Processor: {self.processor}")
        print(f"Price: {self.price}")
        
    
#Create an Object Name Laptop1

laptop1 = Laptop("Asus", "Inter Core i-7", 190000)

# Call Object Method for Display Info

laptop1.display_info()
        
        
