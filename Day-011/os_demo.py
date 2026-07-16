# Demonstrate os module

import os

print("Current Working Directory:")
print(os.getcwd())

print("\nList of Files:")
for file in os.listdir():
    print(file)

folder = "Demo"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"\nFolder '{folder}' created.")
else:
    print(f"\nFolder '{folder}' already exists.")
