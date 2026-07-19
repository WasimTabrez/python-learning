# Banking System using OOP

class BankAccount:

    bank_name = "OpenAI National Bank"

    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.__balance = balance

    def deposit(self):

        try:
            amount = float(input("Enter Amount to Deposit: "))

            if amount <= 0:
                raise ValueError

            self.__balance += amount

            print("Amount deposited successfully.\n")

        except ValueError:
            print("Invalid amount.\n")

    def withdraw(self):

        try:
            amount = float(input("Enter Amount to Withdraw: "))

            if amount <= 0:
                raise ValueError

            if amount > self.__balance:
                print("Insufficient Balance.\n")
                return

            self.__balance -= amount

            print("Amount withdrawn successfully.\n")

        except ValueError:
            print("Invalid amount.\n")

    def transfer(self, receiver):

        try:
            amount = float(input("Enter Amount to Transfer: "))

            if amount <= 0:
                raise ValueError

            if amount > self.__balance:
                print("Insufficient Balance.\n")
                return

            self.__balance -= amount
            receiver.__balance += amount

            print("Transfer successful.\n")

        except ValueError:
            print("Invalid amount.\n")

    def get_balance(self):
        return self.__balance

    def display(self):

        print("-" * 40)
        print("Account No :", self.account_no)
        print("Name       :", self.name)
        print("Balance    :", self.__balance)
        print("-" * 40)


class Bank:

    def __init__(self):
        self.accounts = []

    def search_account(self, account_no):

        for account in self.accounts:
            if account.account_no == account_no:
                return account

        return None

    def create_account(self):

        account_no = input("Enter Account Number: ").strip()

        if self.search_account(account_no):
            print("Account already exists.\n")
            return

        name = input("Enter Customer Name: ").strip()

        try:
            balance = float(input("Enter Initial Balance: "))

            if balance < 0:
                raise ValueError

            self.accounts.append(
                BankAccount(account_no, name, balance)
            )

            print("Account created successfully.\n")

        except ValueError:
            print("Invalid balance.\n")

    def deposit_money(self):

        account_no = input("Enter Account Number: ")

        account = self.search_account(account_no)

        if account:
            account.deposit()
        else:
            print("Account not found.\n")

    def withdraw_money(self):

        account_no = input("Enter Account Number: ")

        account = self.search_account(account_no)

        if account:
            account.withdraw()
        else:
            print("Account not found.\n")

    def transfer_money(self):

        sender_no = input("Sender Account: ")
        receiver_no = input("Receiver Account: ")

        sender = self.search_account(sender_no)
        receiver = self.search_account(receiver_no)

        if sender and receiver:
            sender.transfer(receiver)
        else:
            print("Invalid account number.\n")

    def check_balance(self):

        account_no = input("Enter Account Number: ")

        account = self.search_account(account_no)

        if account:
            print(f"Current Balance : {account.get_balance()}\n")
        else:
            print("Account not found.\n")

    def display_accounts(self):

        if not self.accounts:
            print("No accounts available.\n")
            return

        for account in self.accounts:
            account.display()

    def delete_account(self):

        account_no = input("Enter Account Number: ")

        account = self.search_account(account_no)

        if account:
            self.accounts.remove(account)
            print("Account deleted successfully.\n")
        else:
            print("Account not found.\n")


def menu():

    bank = Bank()

    while True:

        print("\n====== Banking System ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Display Accounts")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                bank.create_account()

            case "2":
                bank.deposit_money()

            case "3":
                bank.withdraw_money()

            case "4":
                bank.transfer_money()

            case "5":
                bank.check_balance()

            case "6":
                bank.display_accounts()

            case "7":
                bank.delete_account()

            case "8":
                print("Thank you!")
                break

            case _:
                print("Invalid Choice.\n")


menu()
