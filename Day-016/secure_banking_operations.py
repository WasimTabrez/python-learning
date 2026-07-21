# Secure Banking Operations using Decorators

import time

balance = 10000
logged_in = False
transaction_log = []


def login_required(function):
    """Allow only logged-in users."""

    def wrapper(*args, **kwargs):

        if not logged_in:
            print("\nPlease login first.\n")
            return

        return function(*args, **kwargs)

    return wrapper


def timer(function):
    """Measure execution time."""

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution Time : {end-start:.6f} seconds\n")

        return result

    return wrapper


def logger(function):
    """Maintain transaction log."""

    def wrapper(*args, **kwargs):

        transaction_log.append(function.__name__)

        return function(*args, **kwargs)

    return wrapper


def login():

    global logged_in

    username = input("Username : ")
    password = input("Password : ")

    if username == "admin" and password == "1234":
        logged_in = True
        print("\nLogin Successful.\n")
    else:
        print("\nInvalid Credentials.\n")


@login_required
@logger
@timer
def deposit():

    global balance

    amount = float(input("Enter Amount : "))

    if amount <= 0:
        print("Invalid Amount\n")
        return

    balance += amount

    print("Deposit Successful")
    print("Balance :", balance)


@login_required
@logger
@timer
def withdraw():

    global balance

    amount = float(input("Enter Amount : "))

    if amount <= 0:
        print("Invalid Amount\n")
        return

    if amount > balance:
        print("Insufficient Balance\n")
        return

    balance -= amount

    print("Withdrawal Successful")
    print("Balance :", balance)


@login_required
@logger
@timer
def check_balance():

    print(f"Current Balance : ₹{balance}")


@login_required
def show_transactions():

    print("\nTransaction History")

    print("----------------------")

    if not transaction_log:
        print("No Transactions")

    else:

        for index, item in enumerate(transaction_log, start=1):
            print(f"{index}. {item}")

    print()


def menu():

    while True:

        print("====== Secure Banking System ======")

        print("1. Login")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter Choice : ")

        match choice:

            case "1":
                login()

            case "2":
                deposit()

            case "3":
                withdraw()

            case "4":
                check_balance()

            case "5":
                show_transactions()

            case "6":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice\n")


menu()
