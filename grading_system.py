# Ask the student to enter their details
student_name = input("Enter student name: ")
mark = int(input("Enter examination mark (0-100): "))
# Check whether the mark is valid and assign a grade
if mark < 0 or mark > 100:
    grade = "Invalid mark"
elif mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark >= 50:
    grade = "C"
elif mark >= 40:
    grade = "D"
else:
    grade = "F"
# Display the student's details and grade
print("\n--- STUDENT GRADING RESULTS ---")
print("Student Name:", student_name)
print("Examination Mark:", mark)
print("Grade:", grade)
