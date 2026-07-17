# Safe Division

try:
    first = float(input("Enter First Number: "))
    second = float(input("Enter Second Number: "))

    print("Result =", first / second)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid number.")
