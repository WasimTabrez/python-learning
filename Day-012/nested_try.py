# Nested Try Example

try:
    number = int(input("Enter Number: "))

    try:
        result = 100 / number
        print("Result =", result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

except ValueError:
    print("Invalid integer.")
