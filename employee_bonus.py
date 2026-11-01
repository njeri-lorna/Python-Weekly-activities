# Ask the employee to enter their details
employee_name = input("Enter employee name: ")
years_of_service = int(input("Enter years of service: "))
performance_rating = int(input("Enter performance rating (1-5): "))
# Check eligibility using the logical AND operator
if years_of_service >= 3 and performance_rating >= 4:
    eligibility = "Employee qualifies for a bonus"
else:
    eligibility = "Employee does not qualify for a bonus"
# Display employee details and eligibility result
print("\n--- EMPLOYEE BONUS DETAILS ---")
print("Employee Name:", employee_name)
print("Years of Service:", years_of_service)
print("Performance Rating:", performance_rating)
print("Eligibility:", eligibility)
