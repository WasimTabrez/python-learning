# Number Processing Pipeline using Generators

def generate_numbers(limit):
    """Generate numbers from 1 to limit."""
    for number in range(1, limit + 1):
        yield number


def even_numbers(numbers):
    """Filter even numbers."""
    for number in numbers:
        if number % 2 == 0:
            yield number


def odd_numbers(numbers):
    """Filter odd numbers."""
    for number in numbers:
        if number % 2 != 0:
            yield number


def square_numbers(numbers):
    """Generate squares."""
    for number in numbers:
        yield number ** 2


def cube_numbers(numbers):
    """Generate cubes."""
    for number in numbers:
        yield number ** 3


def display(generator):
    found = False

    for value in generator:
        print(value)
        found = True

    if not found:
        print("No data available.")

    print()


def menu():

    while True:

        print("====== Number Processing Pipeline ======")
        print("1. Generate Numbers")
        print("2. Filter Even Numbers")
        print("3. Filter Odd Numbers")
        print("4. Generate Squares")
        print("5. Generate Cubes")
        print("6. Display All Numbers")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":

                limit = int(input("Generate numbers up to: "))

                print("\nGenerated Numbers")

                display(generate_numbers(limit))

            case "2":

                limit = int(input("Generate numbers up to: "))

                print("\nEven Numbers")

                display(even_numbers(generate_numbers(limit)))

            case "3":

                limit = int(input("Generate numbers up to: "))

                print("\nOdd Numbers")

                display(odd_numbers(generate_numbers(limit)))

            case "4":

                limit = int(input("Generate numbers up to: "))

                print("\nSquares")

                display(square_numbers(generate_numbers(limit)))

            case "5":

                limit = int(input("Generate numbers up to: "))

                print("\nCubes")

                display(cube_numbers(generate_numbers(limit)))

            case "6":

                limit = int(input("Generate numbers up to: "))

                print("\nAll Numbers")

                display(generate_numbers(limit))

            case "7":

                print("Thank you!")
                break

            case _:

                print("Invalid Choice.\n")


menu()
