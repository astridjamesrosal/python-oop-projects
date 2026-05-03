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
        self.account_balance = self.account_balance + amount
        new_transaction = Transaction(amount, datetime.now(), "Deposit", self.account_balance)
        self.transactions.append(new_transaction)
                
    def withdrawal(self, amount):
        if amount > self.account_balance:
            print("The withdrawal amount exceeds the current balance")
            return
        self.account_balance = self.account_balance - amount
        new_transaction = Transaction(amount, datetime.now(), "Withdrawal", self.account_balance)
        self.transactions.append(new_transaction)