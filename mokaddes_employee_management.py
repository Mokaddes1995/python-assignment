
import os

print("\nWelcome To Employee Salary Management System\n")

# Function 1: Add Employee

def add_employee(name, emp_id, salary):

    with open("employees.txt", "a") as file:

        file.write(f"{name} | {emp_id} | {salary}\n")

    return "Employee Added Successfully!"


# Function 2: View Employees

def view_employees():

    if not os.path.exists("employees.txt"):

        return "\nNo Employee Records Found!"

    with open("employees.txt", "r") as file:

        employees = file.readlines()

    if not employees:

        return "\nNo Employee Records Found!"

    print("\n----- Employee Records -----\n")

    for employee in employees:

        print(employee.strip())

    return "\n----------------------------"


# Main Menu

while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit\n")

    option = input("Choose Option: ")

    if option == "1":

        name = input("\nEnter Name: ")
        emp_id = input("Enter ID: ")
        salary = input("Enter Salary: ")

        result = add_employee(name, emp_id, salary)

        print("\n", result)

    elif option == "2":

        result = view_employees()

        print(result)

    elif option == "3":

        print("\nThank You For Using Employee Management System!")
        break

    else:

        print("\nInvalid Option! Please Try Again.")

    
    