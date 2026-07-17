try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Invalid integer entered.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except Exception as error:
    print("Unexpected Error:", error)
