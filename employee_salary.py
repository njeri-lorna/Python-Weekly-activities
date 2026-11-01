# Ask the user to enter employee details
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary (KSh): "))
deduction = float(input("Enter monthly deduction (KSh): "))
# Calculate housing allowance (10% of basic salary)
housing_allowance = 0.10 * basic_salary
# Calculate gross salary
gross_salary = basic_salary + housing_allowance
# Calculate net salary after deduction
net_salary = gross_salary - deduction
# Display the employee's salary details
print("\n--- EMPLOYEE SALARY DETAILS ---")
print("Employee Name:", employee_name)
print("Basic Salary: KSh", basic_salary)
print("Housing Allowance: KSh", housing_allowance)
print("Gross Salary: KSh", gross_salary)
print("Monthly Deduction: KSh", deduction)
print("Net Salary: KSh", net_salary)
