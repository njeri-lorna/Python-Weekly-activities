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
        print("\nStudent Name:", self.name)
        print("Registration Number:", self.reg_no)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.calculateGrade())


# Main program
student1 = Student()

# Set student information
student1.setStudentDetails(
    "John Kamau",
    "BIT001",
    "Information Technology",
    85
)

# Display student details and grade
student1.displayStudentDetails()
