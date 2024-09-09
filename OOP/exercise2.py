# Create a class BankAccount with attributes balance and methods deposit(amount) and withdraw(amount). Ensure withdraw() prevents the balance from going negative.

class BankAccount:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else: 
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for the withdrawal.")
        
        elif amount <= 0:
            print("Withdrawal amount must be positive.")

        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")

