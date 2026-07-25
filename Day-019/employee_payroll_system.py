# Employee Payroll System using SQLite

import sqlite3


connection = sqlite3.connect("employee_payroll.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL
)
""")

connection.commit()


def add_employee():

    try:

        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        cursor.execute("""
        INSERT INTO employees
        VALUES (?, ?, ?, ?)
        """, (emp_id, name, department, salary))

        connection.commit()

        print("Employee Added Successfully.\n")

    except sqlite3.IntegrityError:
        print("Employee ID Already Exists.\n")

    except ValueError:
        print("Invalid Input.\n")


def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE id=?",
        (emp_id,)
    )

    employee = cursor.fetchone()

    if employee:

        print("\nEmployee Details")

        print("-" * 40)

        print(f"ID         : {employee[0]}")
        print(f"Name       : {employee[1]}")
        print(f"Department : {employee[2]}")
        print(f"Salary     : ₹{employee[3]:,.2f}")

    else:
        print("Employee Not Found.\n")


def update_salary():

    emp_id = int(input("Enter Employee ID: "))
    salary = float(input("Enter New Salary: "))

    try:

        cursor.execute("""
        UPDATE employees
        SET salary=?
        WHERE id=?
        """, (salary, emp_id))

        connection.commit()

        if cursor.rowcount > 0:
            print("Salary Updated Successfully.\n")
        else:
            print("Employee Not Found.\n")

    except sqlite3.Error:

        connection.rollback()

        print("Salary Update Failed.\n")


def delete_employee():

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "DELETE FROM employees WHERE id=?",
        (emp_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Employee Deleted Successfully.\n")
    else:
        print("Employee Not Found.\n")


def display_employees():

    cursor.execute("""
    SELECT *
    FROM employees
    ORDER BY id
    """)

    employees = cursor.fetchall()

    if not employees:

        print("No Employee Records Found.\n")
        return

    print()

    print("=" * 75)

    print(f"{'ID':<6}{'NAME':<20}{'DEPARTMENT':<20}{'SALARY'}")

    print("=" * 75)

    for employee in employees:

        print(
            f"{employee[0]:<6}"
            f"{employee[1]:<20}"
            f"{employee[2]:<20}"
            f"₹{employee[3]:,.2f}"
        )


def total_payroll():

    cursor.execute("""
    SELECT SUM(salary)
    FROM employees
    """)

    payroll = cursor.fetchone()[0]

    if payroll is None:
        payroll = 0

    print(f"\nTotal Payroll : ₹{payroll:,.2f}")


def average_salary():

    cursor.execute("""
    SELECT AVG(salary)
    FROM employees
    """)

    average = cursor.fetchone()[0]

    if average is None:
        average = 0

    print(f"\nAverage Salary : ₹{average:,.2f}")


def menu():

    while True:

        print("\n====== Employee Payroll System ======")

        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Display Employees")
        print("6. Total Payroll")
        print("7. Average Salary")
        print("8. Exit")

        choice = input("Enter Choice: ")

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
                total_payroll()

            case "7":
                average_salary()

            case "8":

                connection.close()

                print("Thank You!")

                break

            case _:
                print("Invalid Choice.\n")


if __name__ == "__main__":
    menu()
