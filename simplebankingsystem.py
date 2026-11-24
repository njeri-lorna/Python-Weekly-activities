# Create BankAccount class
class BankAccount:

    # Initialize account details
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be greater than zero.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    # Display account details
    def displayAccount(self):
        print("\nAccount Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.balance)


# Function to perform transactions
def performTransaction(account, transaction_type, amount):

    if transaction_type == "deposit":
        account.deposit(amount)

    elif transaction_type == "withdraw":
        account.withdraw(amount)

    else:
        print("Invalid transaction type.")


# Main program

# Create two bank account objects
account1 = BankAccount("ACC001", "John Kamau", 10000)
account2 = BankAccount("ACC002", "Mary Jane", 20000)

# Store accounts in a list
accounts = [account1, account2]

# Perform transactions
for account in accounts:

    print("\nAccount:", account.customer_name)

    transaction = input("Enter deposit or withdraw: ").lower()

    try:
        amount = float(input("Enter transaction amount: "))

        performTransaction(account, transaction, amount)

    except ValueError:
        print("Invalid amount. Please enter a number.")


# Display updated account details
print("\nUPDATED BANK ACCOUNT DETAILS")

for account in accounts:
    account.displayAccount()


# Save account details to file
f = open("accounts.txt", "w")

for account in accounts:
    print("Account Number:", account.account_number, file=f)
    print("Customer Name:", account.customer_name, file=f)
    print("Balance:", account.balance, file=f)
    print("----------------------", file=f)

f.close()

print("\nAccount records saved successfully.")
