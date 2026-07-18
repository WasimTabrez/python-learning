# Read All Lines

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:

        lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            print(f"{line_number}. {line}", end="")

except FileNotFoundError:
    print("File not found.")
