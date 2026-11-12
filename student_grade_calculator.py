# Program Name: Student Grade Calculator

print("\nWelcome To Student Grade Calculator")


# Take Input From User Name & Marks

name = input("\nStudent Name: ")

marks = []

subject = ["Math", "Physics", "English"]

print("\nEnter Marks (Marks Must be 0 between 100)\n")

for sub in subject:

    while True:

        mark = int(input(f"{sub}: "))

        # Prevent Invalid Marks

        if mark < 0 or mark > 100:

            print("Invalid Marks! Try Again.")

        else:

            marks.append(mark)

            break


# Total Marks use sum function

total_marks = sum(marks)

# Average Mark

average_mark = total_marks/len(marks)

# Grade Calculate

if average_mark >= 80:

    grade = "A+"

elif average_mark >= 70:

    grade = "A"

elif average_mark >= 60:

    grade = "B"

elif average_mark >= 50:

    grade = 'C'

else:

    grade = "F"

# Print Result

print(f"\n{"=" * 7}Result{"=" * 7} \n")

print(f"Student Name: {name}")

print(f"Total Marks: {total_marks}")

print(f"Average Marks: {average_mark:.2f}")

print(f"Grade: {grade}")

print(f"\n{"*" * 22}\n")


