# ATM Withdrawal

balance = 10000

amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")
