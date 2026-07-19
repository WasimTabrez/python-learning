# Demonstrate encapsulation

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Name    :", self.name)
        print("Balance :", self.__balance)
        print()


account = BankAccount("Wasim", 50000)

account.display()

account.deposit(10000)
account.withdraw(15000)

account.display()

# print(account.__balance)   # Error
