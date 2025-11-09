# BankAccount class to perform basic banking operations

class BankAccount:
    # Constructor to initialize account holder name and balance
    def __init__(self, name, balance=0):
        self.name = name        # Account holder's name
        self.balance = balance  # Initial balance (default is 0)

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    # Method to display current balance
    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ₹{self.balance}")


# Example usage
account1 = BankAccount("Nandini", 1000)
account1.deposit(500)
account1.withdraw(300)
account1.display_balance()
