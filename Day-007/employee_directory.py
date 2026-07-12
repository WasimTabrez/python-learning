# Employee Directory mini project

from functools import wraps


employees = (
    ("EMP001", "Wasim", "Software Engineer"),
    ("EMP002", "John", "QA Engineer"),
    ("EMP003", "Alice", "Project Manager"),
    ("EMP004", "Rahul", "DevOps Engineer"),
    ("EMP005", "Priya", "Data Analyst"),
)

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def show_employees():
    print("\nEmployee Directory")
    print("------------------")

    for index, employee in enumerate(employees, start = 1):
        emp_id, name, designation = employee
        print(f"{index}. {emp_id} | {name} | {designation}")

    print()

@logger
def search_employee():
    name = input("Enter employee name: ")

    found = False

    for employee in employees:
        if employee[1].lower() == name.lower():
            print("\nEmployee Found")
            print("--------------")
            print("ID         :", employee[0])
            print("Name       :", employee[1])
            print("Designation:", employee[2])
            print()

            found = True
            break

    if not found:
        print("Employee not found.\n")

@logger
def display_departments():
    print("\nDepartments")
    print("-----------")

    departments = ()

    for employee in employees:
        department = employee[2]

        if department not in departments:
            departments += (department,)

    for index, department in enumerate(departments, start = 1):
        print(f"{index}. {department}")

    print()
    
    
@logger
def menu():
    while True:
        print("===== Employee Directory =====")
        print("1. Show Employees")
        print("2. Search Employee")
        print("3. Display Departments")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                show_employees()
            case "2":
                search_employee()
            case "3":
                display_departments()
            case "4":
                print("Thank you!")
                break
            case _:
                print("Invalid Choice.\n")

menu()