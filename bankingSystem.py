#Siphokazi Malesa - Banking system

import json #save accounts to file


class BankAccount:
    def __init__(self, acc_name, acc_number, balance=0):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.balance = balance

    #deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited R{amount:.2f}")
        else:
            print("deposit amount must be more than zero.")

    #withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be more than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew R{amount:.2f}")

    #account information
    def display_acc(self):
        print("\n------ Account Details ------")
        print(f"Account Holder : {self.acc_name}")
        print(f"Account Number : {self.acc_number}")
        print(f"Balance        : R{self.balance:.2f}")
        print("-----------------------------")

#-------------------------------------------------------------------------------------------------

#SAVE ACCOUNTS TO FILE
def save_accounts(accounts):
    data = {}

    for acc_num, account in accounts.items():
        data[acc_num] = {
            "name": account.acc_name,
            "balance": account.balance
        }

    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)

#LOAD ACCOUNTS
def load_accounts():
    accounts = {}

    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)

            for acc_num, details in data.items():
                accounts[acc_num] = BankAccount(details["name"], acc_num, details["balance"])

    except FileNotFoundError:
        pass

    return accounts

#----------------------------------------------------------------------------------------------------

#store all accounts - dictionary
accounts = load_accounts()

while True:
    print("\n=== Welcome to SKM Bank ===")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        name = input("Enter your name: ")
        acc_num = input("Enter account number: ")

        if acc_num in accounts:
            print("Account number already exists.")
        else:
            accounts[acc_num] = BankAccount(name, acc_num)
            print("Account successfully created!")
        #save after creating to file
        accounts[acc_num] = BankAccount(name, acc_num)
        save_accounts(accounts)

    elif option == 2:
        acc_num = input("Enter account number: ")

        if acc_num not in accounts:
            print("Account not found")
        else:
            account = accounts[acc_num]

            while True:
                print("\n==== MENU ====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit")

                choice = int(input("Choose an option: "))

                if choice == 1:
                    amount = float(input("Enter amount to deposit: R"))
                    account.deposit(amount)
                    save_accounts(accounts) #save after depositing

                elif choice == 2:
                    amount = float(input("Enter amount to withdraw: R"))
                    account.withdraw(amount)
                    save_accounts(accounts) #save after withdrawin

                elif choice == 3:
                    account.display_acc()

                elif choice == 4:
                    print("Thank you for banking with us.")
                    break

                else:
                    print("Invalid option, try again.")

    elif option == 3:
        print("Thank you for using SKM Bank!")
        break

    else:
        print("Invalid option!")

































