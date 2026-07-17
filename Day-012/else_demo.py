try:
    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division Successful.")
    print("Result:", result)
