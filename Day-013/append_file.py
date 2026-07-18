# Append Data

filename = input("Enter File Name: ")

text = input("Enter Text to Append: ")

try:
    with open(filename, "a") as file:

        file.write(text + "\n")

    print("Data appended successfully.")

except Exception as error:
    print(error)
