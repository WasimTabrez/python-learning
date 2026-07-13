# Store and display employee information

employee = {}

employee["id"] = input("Employee ID: ")
employee["name"] = input("Employee Name: ")
employee["department"] = input("Department: ")
employee["salary"] = float(input("Salary: "))

print()

for key, value in employee.items():
    print(key, ":", value)
