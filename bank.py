accounts = {}

def create_account() :
    try:
        acc_no = int(input("Enter new account number : "))
        if acc_no in accounts:
            print("Account already exist !")
        else:
            name = input("Enter your name : ")
            balance = float(input("Enter initial amount : "))
            accounts[acc_no] = {"name" : name, "balance" : balance}
            print("Account successfully created for ", accounts[acc_no]["name"])
    except ValueError:
        print("ValueError, Balance and amount both should be numbers.")

def deposit_money() :
    try:
        acc_no = int(input("Enter your account number : "))
        if acc_no in accounts :
            balance = float(input("Enter amount : "))
            accounts[acc_no]["balance"] += balance
            print("Balance deposit successful. Balance : ", accounts[acc_no]["balance"])
        else:
            print("Invalid account number.")
    except ValueError:
        print("ValueError, Enter a valid number.")

def withdraw_money():
    try:
        acc_no = int(input("Enter your account number : "))
        if acc_no in accounts:
            amount = float(input("Enter amount : "))
            if amount <= accounts[acc_no]["balance"]:
                accounts[acc_no]["balance"] -= amount
                print("Amount withdraw successful. Balance : ", accounts[acc_no]["balance"])
            else:
                print('Insufficient balance!!')
        else:
            print("Invalid account number")
    except ValueError:
        print("ValueError, Balance should be more than withrawal amount.")

def check_balance():
    try:
        acc_no = int(input("Enter account number : "))
        if acc_no in accounts:
            print("Your account balance is : ", accounts[acc_no]["balance"])
        else:
            print("Invalid account number")
    except ValueError:
        print("ValueError, Enter valid account number.")

def view_all_accounts():
    if accounts:
        print("\n--- All Accounts ---")
        for acc_no, info in accounts.items():
            print(f"Account No: {acc_no}, Name: {info['name']}, Balance: {info['balance']}")
    else:
        print("No accounts available.")

while True:
    print("\n--- Welcome to Python Bank ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View all account info")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == '1' :
        create_account()
    elif choice == '2' :
        deposit_money()
    elif choice == '3' :
        withdraw_money()
    elif choice == '4' :
        check_balance()
    elif choice == '5' :
        view_all_accounts()
    elif choice == '6' :
        print("Thanks for choosing pythonBank. See you soon!!")
        break
    else:
        print("enter a valid choice")