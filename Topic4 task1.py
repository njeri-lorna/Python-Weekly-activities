
# Create a list containing marks in five subjects
marks = [75, 82, 68, 90, 77]

# Display all subject marks
print("Subject Marks:", marks)

# Calculate and display the total marks
total_marks = sum(marks)
print("Total Marks:", total_marks)

# Calculate and display the average mark
average_mark = total_marks / len(marks)
print("Average Mark:", average_mark)

# Display the highest and lowest marks
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

# Modify the mark of the third subject (index 2)
marks[2] = 85

# Display the updated list
print("Updated Marks:", marks)
