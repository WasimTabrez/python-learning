# Menu-driven ATM System using Exception Handling

balance = 10000.0
pin = "1234"
transaction_history = []


def authenticate():
    global pin

    for attempt in range(3):
        entered_pin = input("Enter 4-digit PIN: ")

        if entered_pin == pin:
            print("Login Successful.\n")
            return True

        print(f"Incorrect PIN. Attempts left: {2 - attempt}")

    print("Account Locked.")
    return False


def check_balance():
    print(f"\nAvailable Balance : ₹{balance:.2f}\n")


def deposit():
    global balance

    try:
        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        balance += amount

        transaction_history.append(f"Deposited ₹{amount:.2f}")

        print("Amount deposited successfully.\n")

    except ValueError as error:
        print(error)
        print()


def withdraw():
    global balance

    try:
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > balance:
            raise Exception("Insufficient Balance.")

        balance -= amount

        transaction_history.append(f"Withdrawn ₹{amount:.2f}")

        print("Amount withdrawn successfully.\n")

    except Exception as error:
        print(error)
        print()


def change_pin():
    global pin

    old_pin = input("Enter Current PIN: ")

    if old_pin != pin:
        print("Incorrect PIN.\n")
        return

    new_pin = input("Enter New PIN: ")
    confirm_pin = input("Confirm New PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.\n")
        return

    if new_pin != confirm_pin:
        print("PIN does not match.\n")
        return

    pin = new_pin

    print("PIN changed successfully.\n")


def show_transactions():

    if not transaction_history:
        print("No transactions available.\n")
        return

    print("\nTransaction History")
    print("-------------------")

    for index, transaction in enumerate(transaction_history, start=1):
        print(f"{index}. {transaction}")

    print()


def menu():

    if not authenticate():
        return

    while True:

        print("====== ATM System ======")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            match choice:

                case "1":
                    check_balance()

                case "2":
                    deposit()

                case "3":
                    withdraw()

                case "4":
                    change_pin()

                case "5":
                    show_transactions()

                case "6":
                    print("Thank You!")
                    break

                case _:
                    raise ValueError("Invalid Menu Choice.")

        except KeyboardInterrupt:
            print("\nOperation Cancelled.")

        except Exception as error:
            print(error)
            print()

        finally:
            print("Transaction Completed.\n")


if __name__ == "__main__":
    menu()
