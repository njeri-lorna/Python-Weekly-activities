# Create Student class
class Student:

    # Set student details
    def setStudentDetails(self, name, reg_no, course, mark):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        self.mark = mark

    # Calculate student grade
    def calculateGrade(self):
        if self.mark >= 70 and self.mark <= 100:
            return "A"
        elif self.mark >= 60:
            return "B"
        elif self.mark >= 50:
            return "C"
        elif self.mark >= 40:
            return "D"
        else:
            return "F"

    # Display student details
    def displayStudentDetails(self):
        print("\nName:", self.name)
        print("Registration Number:", self.reg_no)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.calculateGrade())


# Function to display all students
def displayStudents(students):
    for student in students:
        student.displayStudentDetails()


# Main program
students = []

for i in range(3):
    print("\nEnter details for student", i + 1)

    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    course = input("Enter course: ")

    # Handle invalid marks
    while True:
        try:
            mark = float(input("Enter mark: "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Invalid mark. Please enter a number.")

    # Create student object
    student = Student()
    student.setStudentDetails(name, reg_no, course, mark)

    # Add student to list
    students.append(student)


# Display all students
displayStudents(students)


# Save student records to file
f = open("students.txt", "w")

for student in students:
    print("Name:", student.name, file=f)
    print("Registration Number:", student.reg_no, file=f)
    print("Course:", student.course, file=f)
    print("Mark:", student.mark, file=f)
    print("Grade:", student.calculateGrade(), file=f)
    print("----------------------", file=f)

f.close()

print("\nStudent records saved successfully.")
