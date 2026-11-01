# Create a set containing product categories
# Duplicate categories are automatically removed
categories = {"Electronics", "Clothing", "Furniture", "Electronics", "Books", "Food", "Clothing"}
# Display the original set
print("Original Categories:", categories)
# Add a new product category
categories.add("Sports")
# Remove one product category
categories.remove("Food")
# Display the final set
print("Final Categories:", categories)
