PYTHON BANK MANAGEMENT SYSTEM (README)

I made this small Python project called Python Bank to practice working with dictionaries, loops, and functions.
It lets you create accounts, deposit or withdraw money, check balance, and view all account info — all from the command line.

Everything is stored in a Python dictionary instead of a real database, which makes it simple and easy to understand for beginners.

ABOUT THE CODE
1. Using a dictionary to store accounts

All accounts are stored in a dictionary where the key is the account number,
and the value is another dictionary with name and balance.
```
accounts = {
    1001: {"name": "Soumya", "balance": 5000},
    1002: {"name": "Ravi", "balance": 2500}
}
```

This makes it super easy to access or update any account using the account number.

2. Creating a new account

The create_account() function adds a new entry to the accounts dictionary after checking if the account number already exists.
```
def create_account():
    acc_no = int(input("Enter new account number: "))
    if acc_no in accounts:
        print("Account already exist!")
    else:
        name = input("Enter your name: ")
        balance = float(input("Enter initial amount: "))
        accounts[acc_no] = {"name": name, "balance": balance}
        print("Account successfully created for", name)
```
3. Deposit money

The deposit_money() function lets you add money to your balance. It first checks if the account exists.
```
if acc_no in accounts:
    balance = float(input("Enter amount: "))
    accounts[acc_no]["balance"] += balance
    print("Balance deposit successful.")
```

If the account number is wrong, it shows an error message instead.

4. Withdraw money

The withdraw_money() function checks both — if the account exists and if you have enough balance before withdrawing.
```
if amount <= accounts[acc_no]["balance"]:
    accounts[acc_no]["balance"] -= amount
else:
    print("Insufficient balance!!")
```
5. Check balance

The check_balance() function shows the balance for a given account number.
```
print("Your account balance is:", accounts[acc_no]["balance"])
```
6. View all accounts

The view_all_accounts() function prints details of every account stored in the dictionary.
```
for acc_no, info in accounts.items():
    print(f"Account No: {acc_no}, Name: {info['name']}, Balance: {info['balance']}")
```
7. Menu-driven system

The main part of the program runs inside a while True loop.
It keeps showing a menu of options to the user until they choose to exit.
```
while True:
    print("1. Create Account")
    print("2. Deposit Money")
    ...
    choice = input("Enter your choice: ")
```

This makes the program interactive and user-friendly.

EXAMPLE OUTPUT
```
--- Welcome to Python Bank ---
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. View all account info
6. Exit
Enter your choice : 1
Enter new account number : 101
Enter your name : Soumya
Enter initial amount : 5000
Account successfully created for Soumya

--- Welcome to Python Bank ---
Enter your choice : 2
Enter your account number : 101
Enter amount : 1000
Balance deposit successful. Balance : 6000.0

--- Welcome to Python Bank ---
Enter your choice : 6
Thanks for choosing pythonBank. See you soon!!
```
SUMMARY

This small project helped me understand:

How to use dictionaries for storing structured data

How to handle user input and validation

How to use functions to organize code better

How to build a simple menu-based system using loops

It’s not a real banking system of course, but a fun little project for beginners learning Python.
