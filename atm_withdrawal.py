# Store the initial account balance
balance = 50000
# Ask the customer to enter the withdrawal amount
withdrawal = int(input("Enter withdrawal amount (KSh): "))
# Check whether the withdrawal amount is valid
if withdrawal <= 0:
    print("Error: Withdrawal must be greater than zero.")
elif withdrawal > balance:
    print("Error: Insufficient account balance.")
elif withdrawal % 500 != 0:
    print("Error: Amount must be a multiple of KSh 500.")
else:
    # Deduct the withdrawal from the account balance
    balance = balance - withdrawal
    # Display the remaining balance
    print("Withdrawal successful.")
    print("Remaining Balance: KSh", balance)
