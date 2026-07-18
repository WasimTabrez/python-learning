# Read Entire File

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:
        print("\nFile Contents")
        print("-------------")
        print(file.read())

except FileNotFoundError:
    print("File not found.")
