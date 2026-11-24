
# Create BankAccount class
class BankAccount:

    # Initialize account details
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Display account details
    def displayAccount(self):
        print("\nAccount Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.balance)


# Main program
account = BankAccount("123456", "John Kamau", 10000)

# Deposit KSh 5,000
account.deposit(5000)

# Withdraw KSh 2,000
account.withdraw(2000)

# Display account details
account.displayAccount()
