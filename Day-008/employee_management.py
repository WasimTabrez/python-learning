# Menu-driven Employee Management System

employees = {}

def add_employee():
    emp_id = input("Employee ID: ")

    if emp_id in employees:
        print("Employee alread exists.\n")
        return
    
    name = input("Name: ")
    salary = float(input("Salary: "))
    department = input("Department: ")

    employees[emp_id] = {
        "name": name,
        "salary": salary,
        "department": department
    }

    print("Employee added successfully.\n")

def search_employee():
    if not employees:
        print("No employees available.\n")
        return
    
    emp_id = input("Employee ID: ")

    employee = employees.get(emp_id)

    if employee:
        print("\nEmployee Details")
        print("----------------")
        print("Name :",employee["name"])
        print("Salary :", employee["salary"])
        print("Department :", employee["department"])
        print()
    else:
        print("Employee not found.\n")

def update_salary():
    if not employees:
        print("No employees available.\n")
        return
    
    emp_id = input("Employee ID: ")

    if emp_id in employees:
        salary = float(input("New Salary: "))
        employees[emp_id]["salary"] = salary
        print("Salary updated successfully.\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    if not employees:
        print("No employees available.\n")
        return
    
    emp_id = input("Employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.\n")
    else:
        print("Employee not found.\n")

def display_employees():
    if not employees:
        print("No employees available.\n")
        return
    
    print("\nEmployee List")
    print("-------------")

    for emp_id, employee in employees.items():
        print("ID :", emp_id)
        print("Name :", employee["name"])
        print("Salary :", employee["salary"])
        print("Department :", employee["department"])
        print()


while True:
    print("======= Employee Management System =========")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Display Employees")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_employee()
        case "2":
            search_employee()
        case "3":
            update_salary()
        case "4":
            delete_employee()
        case "5":
            display_employees()
        case "6":
            print("Thank you!")
            break
        case _:
            print("Invalid choice.\n")