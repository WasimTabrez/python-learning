# Copy File Contents

source = input("Enter Source File: ")
destination = input("Enter Destination File: ")

try:
    with open(source, "r") as src:
        data = src.read()

    with open(destination, "w") as dest:
        dest.write(data)

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")
