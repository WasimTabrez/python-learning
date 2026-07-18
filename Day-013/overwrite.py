# Overwrite File Contents

filename = input("Enter File Name: ")

print("Enter New Content")
print("-----------------")

text = input()

try:
    with open(filename, "w") as file:

        file.write(text)

    print("File overwritten successfully.")

except Exception as error:
    print(error)
