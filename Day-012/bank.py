# Bank Account Example

balance = 10000


while True:

    print("\n====== Bank ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Choice: ")

    try:

        match choice:

            case "1":
                print("Balance = ₹", balance)

            case "2":
                amount = float(input("Deposit Amount: "))

                if amount <= 0:
                    raise ValueError("Amount must be positive.")

                balance += amount

                print("Deposit Successful.")

            case "3":
                amount = float(input("Withdraw Amount: "))

                if amount <= 0:
                    raise ValueError("Amount must be positive.")

                if amount > balance:
                    raise Exception("Insufficient Balance.")

                balance -= amount

                print("Withdrawal Successful.")

            case "4":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice.")

    except Exception as error:
        print(error)
