# Work with nested dictionaries

employees = {
    "EMP001": {
        "name": "Wasim",
        "salary": 85000
    },
    "EMP002": {
        "name": "John",
        "salary": 9000
    }
}

for emp_id, details in employees.items():
    print(emp_id)
    print(details["name"])
    print(details["salary"])
    print()
