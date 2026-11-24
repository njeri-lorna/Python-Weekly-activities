
# Ask customer to enter withdrawal amount
try:
    amount = int(input("Enter withdrawal amount: "))

    # Display withdrawal amount
    print("Withdrawal amount is:", amount)

except ValueError:
    print("Invalid amount. Please enter a number.")
