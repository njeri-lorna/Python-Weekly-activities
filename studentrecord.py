
# Create a student dictionary
student = {
    "Registration Number": "BIT/001/2026",
    "Student Name": "John Kamau",
    "Course": "Information Technology",
    "Year of Study": 2
}

# Display student name and course
print("Student Name:", student["Student Name"])
print("Course:", student["Course"])

# Change year of study
student["Year of Study"] = 3

# Add email address
student["Email"] = "john@gmail.com"

# Display updated dictionary
print("\nUpdated Student Record:")
print(student)
