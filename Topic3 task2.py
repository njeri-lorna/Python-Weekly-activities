
# Ask the customer to enter the purchase amount
purchase_amount = float(input("Enter total purchase amount (KSh): "))

# Initialize discount to zero
discount = 0.0

# Check whether the customer qualifies for a 15% discount
if purchase_amount >= 10000:
    discount = 0.15 * purchase_amount

# Calculate the final amount after discount
final_amount = purchase_amount - discount

# Display the purchase details
print("\n--- PURCHASE DETAILS ---")
print("Purchase Amount: KSh", purchase_amount)
print("Discount: KSh", discount)
print("Final Amount: KSh", final_amount)
