from employee.salary import calculate_salary
from employee.bonus import calculate_bonus
from employee.tax import calculate_tax
from employee.attendance import attendance_report


def menu():

    while True:

        print("====== Employee Utility ======")
        print("1. Calculate Salary")
        print("2. Calculate Bonus")
        print("3. Calculate Tax")
        print("4. Attendance Report")
        print("5. Exit")

        choice = input("Enter Choice: ")

        match choice:

            case "1":
                calculate_salary()

            case "2":
                calculate_bonus()

            case "3":
                calculate_tax()

            case "4":
                attendance_report()

            case "5":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice\n")


if __name__ == "__main__":
    menu()
