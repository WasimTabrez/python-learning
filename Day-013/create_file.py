# Create a New File

filename = input("Enter File Name: ")

try:
    with open(filename, "x") as file:
        print(f"{filename} created successfully.")


except FileExistsError:
    print("File already exists.")


