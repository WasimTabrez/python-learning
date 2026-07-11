# Search for an element in a list

fruits = ["Apple", "Banana", "Orange", "Mango"]

fruit = input("Enter fruit name: ")

if fruit in fruits:
    print(f"{fruit} is available")
else:
    print(f"{fruit} is not available")