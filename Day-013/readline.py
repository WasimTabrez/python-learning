# Read File Line by Line using readline()

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:

        print(file.readline(), end="")
        print(file.readline(), end="")
        print(file.readline(), end="")

except FileNotFoundError:
    print("File not found.")

