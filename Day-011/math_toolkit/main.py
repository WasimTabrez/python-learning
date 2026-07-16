import arithmetic
import geometry
import statistics
import converter


def calculator():

    a = float(input("First Number: "))
    b = float(input("Second Number: "))

    print("Addition :", arithmetic.add(a, b))
    print("Subtraction :", arithmetic.subtract(a, b))
    print("Multiplication :", arithmetic.multiply(a, b))
    print("Division :", arithmetic.divide(a, b))
    print("Modulus :", arithmetic.modulus(a, b))
    print("Power :", arithmetic.power(a, b))


def area():

    print("\n1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Choice: ")

    if choice == "1":
        r = float(input("Radius: "))
        print("Area =", geometry.circle_area(r))

    elif choice == "2":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("Area =", geometry.rectangle_area(l, w))

    elif choice == "3":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Area =", geometry.triangle_area(b, h))

    else:
        print("Invalid Choice")


def statistics_menu():

    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Maximum :", statistics.maximum(numbers))
    print("Minimum :", statistics.minimum(numbers))
    print("Sum :", statistics.total(numbers))
    print("Average :", statistics.average(numbers))


def converter_menu():

    print("1 Celsius -> Fahrenheit")
    print("2 Fahrenheit -> Celsius")
    print("3 KM -> Miles")
    print("4 Miles -> KM")
    print("5 KG -> Pounds")
    print("6 Pounds -> KG")

    choice = input("Choice: ")

    value = float(input("Value: "))

    match choice:

        case "1":
            print(converter.celsius_to_fahrenheit(value))

        case "2":
            print(converter.fahrenheit_to_celsius(value))

        case "3":
            print(converter.km_to_miles(value))

        case "4":
            print(converter.miles_to_km(value))

        case "5":
            print(converter.kg_to_pounds(value))

        case "6":
            print(converter.pounds_to_kg(value))

        case _:
            print("Invalid Choice")


def menu():

    while True:

        print("\n====== Math Toolkit ======")
        print("1. Basic Calculator")
        print("2. Area Calculator")
        print("3. Unit Converter")
        print("4. Statistics")
        print("5. Exit")

        choice = input("Enter Choice: ")

        match choice:

            case "1":
                calculator()

            case "2":
                area()

            case "3":
                converter_menu()

            case "4":
                statistics_menu()

            case "5":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    menu()
