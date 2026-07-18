# Count Characters

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:

        text = file.read()

        print("Total Characters:", len(text))


except FileNotFoundError:
    print("File not found.")
