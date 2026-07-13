# Demonstrate shallow dictionary copying

employee = {
    "name": "Wasim",
    "salary": 85000
}

copy_employee = employee.copy()

copy_employee["salary"] = 90000

print(employee)

print(copy_employee)