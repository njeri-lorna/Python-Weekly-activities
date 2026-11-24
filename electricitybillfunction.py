# Define the function
def calculate_bill(units, cost_per_unit):
    bill = units * cost_per_unit
    return bill

# Ask the user to enter values
units = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))

# Call the function
total_bill = calculate_bill(units, cost_per_unit)

# Display the electricity bill
print("Your electricity bill is:", total_bill)
