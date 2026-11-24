# Define the function
def calculate_grade(mark):
    if mark >= 70 and mark <= 100:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

# Ask the user to enter a student's mark
mark = float(input("Enter student's mark: "))

# Call the function
grade = calculate_grade(mark)

# Display the grade
print("Student's grade is:", grade)
