# Demonstrate seek() and tell()

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:

        print("Current Position:", file.tell())

        print(file.read(5))

        print("Current Position:", file.tell())

        file.seek(0)

        print("Current Position:", file.tell())

        print(file.read())

except FileNotFoundError:
    print("File not found.")
