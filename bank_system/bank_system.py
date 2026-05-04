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
        new_transaction = Transaction(amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Deposit", self.account_balance)
        self.transactions.append(new_transaction)

                
    def withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        
        if amount > self.account_balance:
            print("The withdrawal amount exceeds the current balance")
            return
        self.account_balance = self.account_balance - amount
        new_transaction = Transaction(amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Withdrawal", self.account_balance)
        self.transactions.append(new_transaction)

    def get_balance(self):
        return self.account_balance
    
    def get_history(self):
        for new_transaction in self.transactions:
            new_transaction.display()

    def display(self):
        print(f"Account Name: {self.owner_name}, Account Number: {self.account_number}, With a current balance of {self.account_balance}")

class Bank:
    def __init__(self, name):
        self.bank_name = name
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, owner_name):
        account_number = self.next_account_number
        new_account = Account(account_number, owner_name, 0)
        self.accounts[account_number] = new_account

        self.next_account_number += 1

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account is None:
            print("The Account Number is invalid")
            return
        return account

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account is None:
            return
        account.deposit(amount)

    def withdrawal(self, account_number, amount):
        account = self.get_account(account_number)
        if account is None:
            return
        account.withdrawal(amount)

    def list_accounts(self):
        for account in self.accounts.values():
            account.display()

bank = Bank("MyBank")
bank.create_account("Astral")
bank.deposit(1, 500)
bank.withdrawal(1, 200)
bank.list_accounts()

account = bank.get_account(1)
account.get_history()