# Menu-driven Employee Database System using Exception Handling

employees = {}


class EmployeeExistsError(Exception):
    pass


class EmployeeNotFoundError(Exception):
    pass


def add_employee():
    try:
        emp_id = input("Enter Employee ID: ").strip()

        if emp_id in employees:
            raise EmployeeExistsError("Employee ID already exists.")

        name = input("Enter Employee Name: ").strip()
        department = input("Enter Department: ").strip()
        salary = float(input("Enter Salary: "))

        if salary <= 0:
            raise ValueError("Salary must be greater than zero.")

        employees[emp_id] = {
            "name": name,
            "department": department,
            "salary": salary
        }

        print("Employee added successfully.\n")

    except Exception as error:
        print(error)
        print()


def search_employee():
    try:
        if not employees:
            raise EmployeeNotFoundError("No employee records available.")

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in employees:
            raise EmployeeNotFoundError("Employee not found.")

        employee = employees[emp_id]

        print("\nEmployee Details")
        print("----------------")
        print("ID         :", emp_id)
        print("Name       :", employee["name"])
        print("Department :", employee["department"])
        print("Salary     :", employee["salary"])
        print()

    except Exception as error:
        print(error)
        print()


def update_salary():
    try:
        if not employees:
            raise EmployeeNotFoundError("No employee records available.")

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in employees:
            raise EmployeeNotFoundError("Employee not found.")

        salary = float(input("Enter New Salary: "))

        if salary <= 0:
            raise ValueError("Salary must be greater than zero.")

        employees[emp_id]["salary"] = salary

        print("Salary updated successfully.\n")

    except Exception as error:
        print(error)
        print()


def delete_employee():
    try:
        if not employees:
            raise EmployeeNotFoundError("No employee records available.")

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in employees:
            raise EmployeeNotFoundError("Employee not found.")

        del employees[emp_id]

        print("Employee deleted successfully.\n")

    except Exception as error:
        print(error)
        print()


def display_employees():

    if not employees:
        print("No employee records available.\n")
        return

    print("\nEmployee List")
    print("-------------")

    for index, (emp_id, employee) in enumerate(employees.items(), start=1):

        print(f"{index}.")
        print("ID         :", emp_id)
        print("Name       :", employee["name"])
        print("Department :", employee["department"])
        print("Salary     :", employee["salary"])
        print()


def count_employees():
    print(f"Total Employees : {len(employees)}\n")


def search_department():

    if not employees:
        print("No employee records available.\n")
        return

    department = input("Enter Department: ").strip().lower()

    found = False

    print()

    for emp_id, employee in employees.items():

        if employee["department"].lower() == department:

            found = True

            print(emp_id)
            print(employee)
            print()

    if not found:
        print("No employees found in this department.\n")


def menu():

    while True:

        print("====== Employee Database ======")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Display Employees")
        print("6. Count Employees")
        print("7. Search by Department")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:

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
                    count_employees()

                case "7":
                    search_department()

                case "8":
                    print("Thank You!")
                    break

                case _:
                    raise ValueError("Invalid menu choice.")

        except KeyboardInterrupt:
            print("\nOperation cancelled.\n")

        except Exception as error:
            print(error)
            print()


if __name__ == "__main__":
    menu()
