# Demonstrate Common os Module Functions

import os

print("Current Working Directory")
print(os.getcwd())

print("\nDirectory Contents")
print("------------------")

for item in os.listdir():
    print(item)

folder = "Demo"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"\n'{folder}' folder created.")
else:
    print(f"\n'{folder}' already exists.")

print("\nFolder Exists:", os.path.exists(folder))

for file in os.listdir():

    if file.endswith(".py"):
        print(file)

print()

filename = input("Enter filename to check: ")

if os.path.isfile(filename):
    print("It is a file.")
elif os.path.isdir(filename):
    print("It is a directory.")
else:
    print("Path not found.")
