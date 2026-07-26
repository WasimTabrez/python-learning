# Student Management System Pro

from student import Student
from database import Database
from validator import *
from file_handler import export_csv, export_json
from logger import info, warning, error
from utils import *


USERNAME = "admin"
PASSWORD = "admin123"


def login():

    title("LOGIN")

    username = input("Username : ")
    password = input("Password : ")

    if username == USERNAME and password == PASSWORD:

        info("Login Successful")

        print("\nLogin Successful.\n")

        return True

    warning("Invalid Login")

    print("\nInvalid Username or Password.\n")

    return False


database = Database()


def add_student():

    try:

        student_id = int(input("Student ID : "))

        if not validate_student_id(student_id):
            print("Invalid Student ID")
            return

        name = input("Name : ")

        if not validate_name(name):
            print("Invalid Name")
            return

        age = int(input("Age : "))

        if not validate_age(age):
            print("Invalid Age")
            return

        course = input("Course : ")

        if not validate_course(course):
            print("Invalid Course")
            return

        marks = float(input("Marks : "))

        if not validate_marks(marks):
            print("Invalid Marks")
            return

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        database.add_student(student)

        info(f"Student Added : {student_id}")

        print("Student Added Successfully.")

    except Exception as e:

        error(str(e))

        print(e)


def search_student():

    student_id = int(input("Enter Student ID : "))

    record = database.search_student(student_id)

    if record:

        line()

        print(record)

        line()

    else:

        print("Student Not Found.")


def update_student():

    student_id = int(input("Student ID : "))

    marks = float(input("New Marks : "))

    database.update_marks(student_id, marks)

    info(f"Marks Updated : {student_id}")

    print("Record Updated.")


def delete_student():

    student_id = int(input("Student ID : "))

    database.delete_student(student_id)

    warning(f"Student Deleted : {student_id}")

    print("Record Deleted.")


def display_students():

    records = database.get_all_students()

    display_students(records)


def reports():

    records = database.get_all_students()

    total = len(records)

    if total == 0:

        print("No Records")

        return

    highest = max(records, key=lambda x: x[4])

    lowest = min(records, key=lambda x: x[4])

    average = sum(student[4] for student in records) / total

    title("REPORT")

    print(f"Total Students : {total}")

    print(f"Average Marks  : {average:.2f}")

    print(f"Highest Marks  : {highest[4]} ({highest[1]})")

    print(f"Lowest Marks   : {lowest[4]} ({lowest[1]})")


def export_data():

    records = database.get_all_students()

    export_csv("students.csv", records)

    export_json("students.json", records)

    info("Data Exported")


def main():

    if not login():
        return

    while True:

        title("Student Management System Pro")

        menu()

        choice = input("\nEnter Choice : ")

        match choice:

            case "1":
                add_student()

            case "2":
                search_student()

            case "3":
                update_student()

            case "4":
                delete_student()

            case "5":
                display_students()

            case "6":
                export_data()

            case "7":
                export_data()

            case "8":
                reports()

            case "9":

                database.close()

                info("Application Closed")

                print("\nThank You!")

                break

            case _:

                print("Invalid Choice.")

        pause()


if __name__ == "__main__":
    main()
