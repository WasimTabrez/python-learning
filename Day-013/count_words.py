# Count Number of Words

filename = input("Enter File Name: ")

try:
    with open(filename, "r") as file:

        text = file.read()

        words = text.split()

        print("Total Words:", len(words), words)

except FileNotFoundError:
    print("File not found.")
