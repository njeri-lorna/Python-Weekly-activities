# Parent class
class Employee:

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def displayEmployee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)


# Child class
class Lecturer(Employee):

    def __init__(self, name, employee_id, subject):
        super().__init__(name, employee_id)
        self.subject = subject

    def displayLecturer(self):
        self.displayEmployee()
        print("Teaching Subject:", self.subject)


# Main program
lecturer1 = Lecturer("John Kamau", "EMP001", "Python Programming")

lecturer1.displayLecturer()
