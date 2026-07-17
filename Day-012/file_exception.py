# File Exception Example

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("Permission denied.")

except Exception as error:
    print(error)
