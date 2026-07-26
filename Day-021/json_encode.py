import json

student = {
    "id": 101,
    "name": "Wasim",
    "course": "Python",
    "marks": 95
}

json_data = json.dumps(student, indent=4)

print(json_data)
