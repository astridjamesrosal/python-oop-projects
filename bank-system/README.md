# Bank System 

## Features
- Create an Account
- Deposit Money to an Account
- Withdraw Money from an Account
- View Account
- View Transaction History of an Account
- View the list of all Accounts

## How to Run
- Clone the repository
- Navigate to the bank-system folder
- Run `python main.py`

## What I learned
- Applied Class Composition - Transaction, Account, and Bank each handle a distinct responsibility with their assigned attributes and methods through which they interact with each other.
- Applied Encapsulation to keep the data and logic that acts on it inside the class that owns it. No unnecessary data for the main loop that it doesn't need to run.
- Implemented ID Collision prevention using the max ID method. This ensures that the next id that will be assigned will be plus 1 of the highest existing ID in the list.

## Preview
![Main Menu](./Bank_Preview_1.jpg.png)
![Creating an Account](./Bank_Preview_2.jpg.png)
![Deposit to an Account](./Bank_Preview_3.jpg.png)
![Withdraw from an Account](./Bank_Preview_4.jpg.png)
![View an Account](./Bank_Preview_5.jpg.png)
![View Transaction History](./Bank_Preview_6.jpg.png)
![View All Accounts](./Bank_Preview_7.jpg.png)