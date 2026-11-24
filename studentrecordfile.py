
# Open file in write mode
f = open("students.txt", "w")

# Write student records
print("Name: John Kamau", file=f)
print("Registration Number: BIT001", file=f)
print("Course: ICT", file=f)
print("Mark: 85", file=f)

print("\nName: Mary Jane", file=f)
print("Registration Number: BIT002", file=f)
print("Course: ICT", file=f)
print("Mark: 75", file=f)

print("\nName: Peter Mwangi", file=f)
print("Registration Number: BIT003", file=f)
print("Course: ICT", file=f)
print("Mark: 65", file=f)

# Close the file
f.close()

print("Student records saved successfully.")
