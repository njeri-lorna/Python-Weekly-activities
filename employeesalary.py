
# Create employees dictionary
employees = {
    "John": 30000,
    "Mary": 40000,
    "Peter": 35000,
    "Jane": 45000,
    "David": 50000
}

# Display all employee names and salaries
print("Employee Salary Records:")
for name, salary in employees.items():
    print(name, ":", salary)

# Update salary of an employee
employees["John"] = 35000

# Add a new employee
employees["Grace"] = 40000

# Calculate total salary
total_salary = sum(employees.values())

# Display updated records and total salary
print("\nUpdated Employee Records:")
for name, salary in employees.items():
    print(name, ":", salary)

print("\nTotal Salary Payable:", total_salary)
