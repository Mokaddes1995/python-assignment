# Section 1: Programming Tasks

# Task 1 (Basic Class): Create a class named Laptop with properties for brand, processor, and price. 
# Create an object of this class and print all its details.

class Laptop:
    
    # Constructor Method
    
    def __init__(self, brand, processor, price):
        self.brand = brand
        self.processor = processor
        self.price = price