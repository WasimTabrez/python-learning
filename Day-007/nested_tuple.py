# Work with nested tuples

employees = (
    ("EMP001", "Wasim", "Software Engineer"),
    ("EMP002", "John", "QA Engineer"),
    ("EMP003", "Alice", "Project Manager"),
)

print("Employee Details")
print("----------------")

for emp_id, name, designation in employees:
    print(emp_id, "-", name, "-", designation)

