# Read and Write JSON Files

# import json

# filename = "student.json"

# student = {
#     "id": 101,
#     "name": "Wasim",
#     "marks": 95,
#     "city": "Bengaluru"
# }

# # Write JSON

# with open(filename, "w") as file:
#     json.dump(student, file, indent=4)

# print("JSON file created successfully.\n")

# # Read JSON

# with open(filename, "r") as file:
#     data = json.load(file)

# print("Student Details")
# print("---------------")

# for key, value in data.items():
#     print(f"{key} : {value}")


# List of Objects

import json

employees = [
    {
        "id": "EMP001",
        "name": "Wasim",
        "salary": 85000
    },
    {
        "id": "EMP002",
        "name": "John",
        "salary": 70000
    }
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("employees.json", "r") as file:

    data = json.load(file)

    print()

    for employee in data:
        print(employee)
