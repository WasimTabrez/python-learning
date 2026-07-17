# Custom Exception Example

class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    pass


try:
    age = int(input("Enter Age: "))

    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

    print("Eligible.")

except InvalidAgeError as error:
    print(error)

except ValueError:
    print("Please enter a valid age.")
