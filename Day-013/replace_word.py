# Replace Word in File

filename = input("Enter File Name: ")

old_word = input("Enter Word to Replace: ")
new_word = input("Enter New Word: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    updated_text = text.replace(old_word, new_word)

    with open(filename, "w") as file:
        file.write(updated_text)

    print("Word replaced successfully.")

except FileNotFoundError:
    print("File not found.")
