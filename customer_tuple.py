# Create a tuple containing customer information
customer = ("John Kamau", "CUS001", "0712345678", "john@example.com")
# Display the complete tuple
print("Customer Details:", customer)
# Access and display the customer's name (index 0)
print("Customer Name:", customer[0])
# Access and display the customer's telephone number (index 2)
print("Telephone Number:", customer[2])
# Display the number of items in the tuple
print("Number of Items:", len(customer))
# Attempt to modify the telephone number
# This will produce a TypeError because tuples are immutable
try:
    customer[2] = "0798765432"
except TypeError:
    print("Modification failed: Tuples cannot be modified.")
