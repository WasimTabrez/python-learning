from employee import Employee
from employee_database import EmployeeDatabase
from employee_file_handler import *
from employee_logger import log
from employee_utils import *

database = EmployeeDatabase()

while True:

    title("Employee Management System Pro")

    print("1.Add Employee")
    print("2.Display Employees")
    print("3.Search Employee")
    print("4.Update Salary")
    print("5.Delete Employee")
    print("6.Total Payroll")
    print("7.Average Salary")
    print("8.Export CSV")
    print("9.Export JSON")
    print("10.Exit")

    choice = input("Choice : ")

    match choice:

        case "1":

            employee = Employee(

                int(input("ID : ")),

                input("Name : "),

                input("Department : "),

                input("Designation : "),

                float(input("Salary : "))

            )

            database.add_employee(employee)

            log("Employee Added")

        case "2":

            display(

                database.all_employees()

            )

        case "3":

            employee = database.search(

                int(input("Employee ID : "))

            )

            print(employee)

        case "4":

            database.update_salary(

                int(input("Employee ID : ")),

                float(input("New Salary : "))

            )

            log("Salary Updated")

        case "5":

            database.delete(

                int(input("Employee ID : "))

            )

            log("Employee Deleted")

        case "6":

            print(

                f"\nTotal Payroll : ₹{database.total_payroll():,.2f}"

            )

        case "7":

            print(

                f"\nAverage Salary : ₹{database.average_salary():,.2f}"

            )

        case "8":

            export_csv(

                database.all_employees()

            )

            print("CSV Exported")

        case "9":

            export_json(

                database.all_employees()

            )

            print("JSON Exported")

        case "10":

            database.close()

            break

        case _:

            print("Invalid Choice")
