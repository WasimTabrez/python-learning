# Age Validator

try:
    age = int(input("Enter Age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 18:
        raise Exception("You are not eligible.")

    print("Eligible.")

except Exception as error:
    print(error)
