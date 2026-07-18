# Write to a File

filename = input("Enter File Name: ")

text = input("Enter Text: ")

try:
    with open(filename, "w") as file:
        file.write(text)

    print("Data written successfully.")

except Exception as error:
    print(error)
