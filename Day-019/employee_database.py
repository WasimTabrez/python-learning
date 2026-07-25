# Employee Database using SQLite

import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

connection.commit()


def add_employee():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        (emp_id, name, department, salary)
    )
    connection.commit()
    print("Employee Added Successfully.\n")


def display_employees():
    cursor.execute("SELECT * FROM employees")

    records = cursor.fetchall()

    if records:
        print("\nEmployee Records\n")

        for employee in records:
            print(employee)
    else:
        print("No Employees Found.\n")


while True:

    print("\n====== Employee Database ======")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    match choice:

        case "1":
            add_employee()

        case "2":
            display_employees()

        case "3":
            connection.close()
            print("Thank You!")
            break

        case _:
            print("Invalid Choice")
