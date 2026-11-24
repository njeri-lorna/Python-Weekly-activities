# Create inventory dictionary
inventory = {
    "Sugar": 20,
    "Rice": 15,
    "Milk": 30,
    "Bread": 25,
    "Cooking Oil": 10
}

# Display quantity of a specified product
print("Quantity of Rice:", inventory["Rice"])

# Add a new product
inventory["Flour"] = 18

# Update quantity of an existing product
inventory["Sugar"] = 35

# Remove one product
inventory.pop("Bread")

# Display final inventory
print("\nFinal Inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)
