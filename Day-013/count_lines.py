# Count Number of Lines

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:

        count = 0

        for line in file:
            count += 1

        print("Total Lines:", count)

except FileNotFoundError:
    print("File not found.")
