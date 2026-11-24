# Open sales.txt in append mode
f = open("sales.txt", "a")

# Ask user to enter sales information
product = input("Enter product name: ")
quantity = int(input("Enter quantity sold: "))
amount = float(input("Enter total sales amount: "))

# Write sales record to file
print("Product:", product, file=f)
print("Quantity Sold:", quantity, file=f)
print("Total Sales Amount:", amount, file=f)
print("----------------------", file=f)

# Close the file
f.close()

print("Sales record saved successfully.")
