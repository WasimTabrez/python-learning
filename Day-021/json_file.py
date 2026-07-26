import json

student = {
    "id": 101,
    "name": "Wasim",
    "course": "Python",
    "marks": 95
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file written successfully.")

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
