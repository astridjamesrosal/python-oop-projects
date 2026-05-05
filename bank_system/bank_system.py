from datetime import datetime                                           #Imports the datetime tools in order to indicate the time.

class Transaction:                                                      #Creates a blueprint called Transaction,
    def __init__(self, amount, date, transaction, balance):             #Initializes the ATTRIBUTES automatically after being created.
        self.amount = amount                                            #"self.amount" stores the value of "amount" on the object.
        self.timestamp = date                                           #"self.timestamp" stores the value of "date" on the object.
        self.transaction_type = transaction                             #"self.transaction_type" stores the value of "transaction" on the object.
        self.remaining_balance = balance                                #"self.remaining_balance" stores the value of "balance" on the object.
    
    def display(self):                                                  #Display the transaction attributes, it needs self because it is how each object refers to their own specific data.
        print(f"You have successfully {self.transaction_type} {self.amount}. On this date: ({self.timestamp}), you currently have: {self.remaining_balance} in your account. Thank you.")
        
class Account:                                                          #Creates a blueprint called Account.
    def __init__(self, account, name, balance):                         #Initializes the ATTRIBUTES automatically after being created.
        self.account_number = account                                   #"self.account_number" stores the value of "account" on the object.
        self.owner_name = name                                          #"self.owner_name" stores the value of "name" on the object.
        self.account_balance = balance                                  #"self.account_balance" stores the value of "balance" on the object.
        self.transactions = []                                          #"self.transactions" stores the values on a list.

    def deposit(self, amount):                                          #Defines a method that lets the user deposit and needs an amount.
        if amount <= 0:                                                 #If the amount is less than or equal to zero.
            print("Deposit amount must be positive")                   
            return                                                      #Exit and don't process invalid amount.
        
        self.account_balance = self.account_balance + amount            #First get the account balance and add the amount to it.
        new_transaction = Transaction(amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Deposit", self.account_balance)    #Stores it in a new_transaction OBJECT that contains all the information.
        self.transactions.append(new_transaction)                       #Adds the new_transaction to the transactions list.

                
    def withdrawal(self, amount):                                       #Defines a method that lets the user withdraw and needs an amount.
        if amount <= 0:                                                 #If amount is less than or equal to zero.
            print("Withdrawal amount must be positive")
            return                                                      #Exit and don't process invalid amount.
        
        if amount > self.account_balance:                               #If the amount is greater than the current balance.
            print("The withdrawal amount exceeds the current balance")
            return                                                      #Exit and don't process invalid amount.
        
        self.account_balance = self.account_balance - amount            #First get the account balance and deduct the amount to it.
        new_transaction = Transaction(amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Withdrawal", self.account_balance)     #Stores it in a new_transaction OBJECT that contains all the information.
        self.transactions.append(new_transaction)                       #Adds the new_transaction to the transactions list.


    def get_balance(self):                                              #Defines a method that lets the user get the balance of their account
        return self.account_balance                                     #Sends the current balance back to the menu or method that called it.
    
    def get_history(self):                                              #Defines a method that lets the user view the transactions made.
        for new_transaction in self.transactions:                       #Loops through every new_transaction in self.transactions
            new_transaction.display()                                   #Display all of those new_transactions.

    def display(self):                                                  #Defines a method that displays all the necessary information of the user.
        print(f"Account Name: {self.owner_name}, Account Number: {self.account_number}, With a current balance of {self.account_balance}")

class Bank:                                                             #Creates a blueprint called Bank.
    def __init__(self, name):                                           #Initializes the ATTRIBUTES automatically after being created.
        self.bank_name = name                                           #"self.bank_name" stores the values of "name" on the object.
        self.accounts = {}                                              #"self.accounts" stores all accounts as a dictionary — account_number maps to Account object.
        self.next_account_number = 1                                    #"self.next_account_number" assigns the first account a number 1.

    def create_account(self, owner_name):                               #Defines a method that lets the user create an account and needs a owner_name.
        account_number = self.next_account_number                       #Assigns the new_account the numer 1 or increments it based on the number of accounts.
        new_account = Account(account_number, owner_name, 0)            #Stores the Account with its account number, owner name, and balance in the new_account object.
        self.accounts[account_number] = new_account                     #Uses the account_number in the self.accounts when searching for that new_account.

        self.next_account_number += 1                                   #Everytime there is a new account their account number increments by 1.

    def get_account(self, account_number):                              #Defines a method that lets the user view their account.
        account = self.accounts.get(account_number)                     #They get the account object through the account_number.
        if account is None:                                             #If the account number doesn't exist in the system.
            print("The Account Number is invalid")
            return                                                      #Exit and don't process invalid input
        return account                                                  #Returns to the account if everything is fine.

    def deposit(self, account_number, amount):                          #Defines a method that lets the user deposit through account_number and amount.
        account = self.get_account(account_number)                      #They get the account object through the account_number.
        if account is None:                                             #If the account number doesn't exist in the system.
            return                                                      #Exit the method.
        account.deposit(amount)                                         #If there is an account, deposit to it using amount.

    def withdrawal(self, account_number, amount):                       #Defines a method that lets the user withdraw through account_number and amount.
        account = self.get_account(account_number)                      #They get the account object through the account_number.
        if account is None:                                             #If the account number doesn't exist in the system.
            return                                                      #Exit the method.
        account.withdrawal(amount)                                      #If there is an account, withdraw to it using amount.

    def list_accounts(self):                                            #Defines a method that lets the user view all the accounts.
        for account in self.accounts.values():                          #Loops through every account in self.accounts.values() - .values() gives us the Account objects instead of the account numbers.
            account.display()                                           #Display all the accounts.

bank = Bank("Astral Bank")                                              #Creates the Bank instance that the entire program runs on.
print("Welcome to Astral, your money safe in the galaxy!")              #Introductory Message when the program runs.

while True:                                                             #Main Loop. Keeps asking the questions until the user exits.

    print("1. Create an Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Account")
    print("5. View Transaction History")
    print("6. List of all Account")
    print("7. Exit")

    choice = input("Please choose a number: ")                          #Ask the user to choose a number based on what they want to do.

    if choice == "1":                                                   #If the user choose 1.
        owner_name = input("Enter your Name: ")                         #Stores the name inputed by the User to the owner_name Object.
        bank.create_account(owner_name)                                 #Creates an account for the user with their Account Name.
        print(f"Account created successfully. Your account number is: {bank.next_account_number - 1}")

    elif choice == "2":                                                 #If the user choose 2.
        account_number = int(input("Enter your account number: "))      #Ask the user for the account number.
        account = bank.get_account(account_number)                      #Gets the account through the account_number.
        if account:                                                     #If there is an account.
            amount = float(input("Enter the amount you would like to deposit: "))   #Ask the user for the amount they would like to deposit.
            bank.deposit(account_number, amount)                        #Deposit to the account using the account_number and amount.
            print(f"Successfully deposited {amount}.")

    elif choice == "3":                                                 #If the user choose 3.
        account_number = int(input("Enter your account number: "))      #Ask the user for the account number.
        account = bank.get_account(account_number)                      #Gets the account through the account_number.
        if account:                                                     #If there is an account.
            amount = float(input("Enter the amount you would like to withdraw: "))   #Ask the user for the amount they would like to withdraw.
            bank.withdrawal(account_number, amount)                     #Withdraw to the account using the account_number and amount.
            print(f"Successfully withdrew {amount}.")

    elif choice == "4":                                                 #If the user choose 4.
        account_number = int(input("Enter your account number: "))      #Ask the user for the account number.
        account = bank.get_account(account_number)                      #Gets the account through the account_number.
        if account:                                                     #If there is an account.
            account.display()                                           #Display the user's account.

    elif choice == "5":                                                 #If the user choose 5.
        account_number = int(input("Enter your account number: "))      #Ask the user for the account_number.
        account = bank.get_account(account_number)                      #Gets the account through the account_number.
        if account:                                                     #If there is an account.
            account.get_history()                                       #Display the user's account transaction history.

    elif choice == "6":                                                 #If the user choose 6.
        bank.list_accounts()                                            #List all the bank accounts.

    elif choice == "7":                                                 #If the user choose 7.
        exit()                                                          #Exits the program.