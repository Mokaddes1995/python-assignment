class Student:
    
    # Constructor Method
    
    def __init__(self, name, department, marks):
        
        self.name = name
        self.department = department
        self.marks = marks
        
    # Instance Method
    
    # Display
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade()}")
        print(self.average_marks())
    
    # Average Marks Method
    
    def average_marks(self):
        
        average = sum(self.marks)/len(self.marks)
        
        return f'Average Marks: {average}'
    
    
    # Grade Method
    
    def grade(self):
        
        avg = sum(self.marks) / len(self.marks)
        
        if avg >= 80:
            return 'A+'
        elif avg >= 70:
            return 'A'
        elif avg >= 60:
            return 'A-'
        elif avg >= 50:
            return "B"
        elif avg >= 40:
            return 'C'
        elif self.marks >= 33:
            return "D"
        else:
            return "F"
    
    
student1 = Student('Rahim', 'CSE', [90,70,50])

student1.display()


from datetime import datetime


maturity_year = 1

start_year = 2025

print(start_year)

maturity_year = start_year + maturity_year

print(maturity_year)


def is_mature():
    current_year = datetime.now().year
    return current_year >= maturity_year

print(is_mature())


if not is_mature():
    print("Not Mature")
else:
    print("Mature")