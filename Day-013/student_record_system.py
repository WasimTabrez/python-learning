# Menu-driven Student Record File System

import os

FILENAME = "students.txt"


def add_student():
    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.\n")
        return

    students = []

    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            students = [line.strip() for line in file]

    if name in students:
        print("Student already exists.\n")
        return

    with open(FILENAME, "a") as file:
        file.write(name + "\n")

    print("Student added successfully.\n")


def view_students():
    if not os.path.exists(FILENAME):
        print("No student records found.\n")
        return

    with open(FILENAME, "r") as file:
        students = [line.strip() for line in file if line.strip()]

    if not students:
        print("No student records found.\n")
        return

    print("\nStudent List")
    print("------------")

    for roll, student in enumerate(students, start=1):
        print(f"{roll}. {student}")

    print()


def search_student():
    if not os.path.exists(FILENAME):
        print("No student records found.\n")
        return

    name = input("Enter Student Name: ").strip()

    with open(FILENAME, "r") as file:
        students = [line.strip() for line in file]

    if name in students:
        print(f"{name} found.\n")
    else:
        print("Student not found.\n")


def update_student():
    if not os.path.exists(FILENAME):
        print("No student records found.\n")
        return

    old_name = input("Enter Existing Student Name: ").strip()
    new_name = input("Enter New Student Name: ").strip()

    with open(FILENAME, "r") as file:
        students = [line.strip() for line in file]

    if old_name not in students:
        print("Student not found.\n")
        return

    if new_name in students:
        print("New student name already exists.\n")
        return

    index = students.index(old_name)
    students[index] = new_name

    with open(FILENAME, "w") as file:
        for student in students:
            file.write(student + "\n")

    print("Student updated successfully.\n")


def delete_student():
    if not os.path.exists(FILENAME):
        print("No student records found.\n")
        return

    name = input("Enter Student Name: ").strip()

    with open(FILENAME, "r") as file:
        students = [line.strip() for line in file]

    if name not in students:
        print("Student not found.\n")
        return

    students.remove(name)

    with open(FILENAME, "w") as file:
        for student in students:
            file.write(student + "\n")

    print("Student deleted successfully.\n")


def count_students():
    if not os.path.exists(FILENAME):
        print("Total Students: 0\n")
        return

    with open(FILENAME, "r") as file:
        students = [line.strip() for line in file if line.strip()]

    print(f"Total Students: {len(students)}\n")


def menu():
    while True:

        print("====== Student Record System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Count Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_student()

            case "2":
                view_students()

            case "3":
                search_student()

            case "4":
                update_student()

            case "5":
                delete_student()

            case "6":
                count_students()

            case "7":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice.\n")


menu()
