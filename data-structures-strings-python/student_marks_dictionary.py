# Task 1: Create a Dictionary of Student Marks

# Creating a dictionary of students and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 76
}

# Taking student name as input
name = input("Enter the student's name: ").strip()

# Retrieving marks using dictionary lookup
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
