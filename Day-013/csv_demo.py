# Read and Write CSV Files

# import csv

# filename = "students.csv"

# students = [
#     ["ID", "Name", "Marks"],
#     ["101", "Wasim", "95"],
#     ["102", "John", "88"],
#     ["103", "Alice", "91"]
# ]

# # Write CSV
# with open(filename, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(students)

# print("CSV file created successfully.\n")

# # Read CSV
# print("Student Records")
# print("---------------")

# with open(filename, "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# Dictionary CSV

import csv

filename = "employees.csv"

employees = [
    {"ID": "EMP001", "Name": "Wasim", "Department": "Software"},
    {"ID": "EMP002", "Name": "John", "Department": "QA"},
    {"ID": "EMP003", "Name": "Alice", "Department": "HR"}
]

with open(filename, "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["ID", "Name", "Department"]
    )

    writer.writeheader()
    writer.writerows(employees)

print("Employee CSV Created.\n")

with open(filename, "r") as file:

    reader = csv.DictReader(file)

    for employee in reader:
        print(employee)
