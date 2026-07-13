# Search for a key in a dictionary

student = {
    "name": "Wasim",
    "age": 28,
    "course": "Python"
}

key = input("Enter key: ")

if key in student:
    print("Value:", student[key])
else:
    print("Key not found.")
