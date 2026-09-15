# Section 1: Programming Tasks

# Task 1 (Basic Class): Create a class named Laptop with properties for brand, processor, and price. 
# Create an object of this class and print all its details.

class Laptop:
    
    # Constructor Method
    
    def __init__(self, brand, processor, price):
        self.brand = brand
        self.processor = processor
        self.price = price
        
    # Instance Method for Printing Information
    
    def display_info(self):
        
        print(f"Brand: {self.brand}")
        print(f"Processor: {self.processor}")
        print(f"Price: {self.price}")
        
    
# Create an Object Named Laptop1

laptop1 = Laptop("Asus", "Intel Core i7", 190000)

# Call Object Method for Display Information

laptop1.display_info()


# Task 2

''' 
Task 2 (Method Implementation): Create a class Circle that takes radius as a parameter in the __init__ method. 
Add a method called calculated_area that returns the area of the circle (Formula: π𝑟2  ) and a  method called 
calculated_perimeter that returns the perimeter of the circle (Formula: 2πr).
'''

# Import Math Module for pi

import math

class Circle:
    
    # Constructor Method
    
    def __init__(self, radius):
        
        # Take Radius Parameter
        
        self.radius = radius
        
    # Instance Method for Calculated Area
    
    def calculated_area(self):
        
        area = math.pi * self.radius ** 2
        
        return area
    
    # Instance Method for Calculated Perimeter
    
    def calculated_perimeter(self):
        
        perimeter = 2 * math.pi * self.radius
        
        return perimeter
    
    # Instance Method for Show Information
    
    def show_information(self):
        
        # Call Calculated Area Method
        
        print(f"Area: {self.calculated_area():.6f}")
        
        # Call Calculated Perimeter Method 
        
        print(f"Perimeter: {self.calculated_perimeter():.6f}")
        

"Create an Object"

circle1 = Circle(50)

# Display Information

circle1.show_information()


# Task 3

'''
Task 3 (Object Manipulation): Create a Player class with name and score. 
Create an object, print the initial score, update the score with new value, and print the updated score.
'''

class Player:
    
    # Constructor Method
    
    def __init__(self, name, score):
        
        self.name = name
        self.score = score
        
    # Create Instance Method for Update Score
    
    def update_score(self, new_score):
        
        # Give Validation for Negative Value
        
        if new_score < 0:
            
            raise ValueError ('Score Must Be 0 and Above!!')
        
        else:
            
            self.score = new_score
            
            print(f"Updated Score: {self.score}")
    
    # Instance Method for Printing Information
    
    def show_info(self):
        
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        
    
# Create an Object

player1 = Player('Mahir', 30)

# Print Name and Initial Score

player1.show_info()

# Print Updated Score

player1.update_score(60)


