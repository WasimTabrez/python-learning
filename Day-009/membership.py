# Check whether an element exists in a set

fruits = {"Apple", "Banana", "Mango", "Orange"}

fruit = input("Enter fruit name: ")

if fruit in fruits:
    print(f"{fruit} is available.")
else:
    print(f"{fruit} is not available.")

