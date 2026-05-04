from datetime import datetime

class Transaction:
    def __init__(self, amount, date, transaction, balance):
        self.amount = amount
        self.timestamp = date
        self.transaction_type = transaction
        self.remaining_balance = balance
    
    def display(self):
        print(f"You have successfully {self.transaction_type} {self.amount}. On this date: ({self.timestamp}), you currently have: {self.remaining_balance} in your account. Thank you.")
        
class Account: 
    def __init__(self, account, name, balance):
        self.account_number = account
        self.owner_name = name
        self.account_balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        
        self.account_balance = self.account_balance + amount
        new_transaction = Transaction(amount, datetime.now(), "Deposit", self.account_balance)
        self.transactions.append(new_transaction)

                
    def withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        
        if amount > self.account_balance:
            print("The withdrawal amount exceeds the current balance")
            return
        self.account_balance = self.account_balance - amount
        new_transaction = Transaction(amount, datetime.now(), "Withdrawal", self.account_balance)
        self.transactions.append(new_transaction)

    def get_balance(self):
        return self.account_balance
    
    def get_history(self):
        for new_transaction in self.transactions:
            new_transaction.display()

    def display(self):
        print(f"Account Name: {self.owner_name}, Account Number: {self.account_number}, With a current balance of {self.account_balance}")