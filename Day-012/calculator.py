# Calculator with Exception Handling

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:

    print("\n====== Calculator ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank You!")
        break

    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        match choice:

            case "1":
                print("Result =", add(num1, num2))

            case "2":
                print("Result =", subtract(num1, num2))

            case "3":
                print("Result =", multiply(num1, num2))

            case "4":
                print("Result =", divide(num1, num2))

            case _:
                print("Invalid Choice.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Please enter valid numbers.")

    except Exception as error:
        print(error)
