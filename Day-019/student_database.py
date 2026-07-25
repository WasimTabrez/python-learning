# Student Database using SQLite

import sqlite3

connection = sqlite3.connect("student_management.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks REAL
)
""")

connection.commit()


def add_student():

    student_id = int(input("ID: "))
    name = input("Name: ")
    course = input("Course: ")
    marks = float(input("Marks: "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, course, marks)
    )

    connection.commit()

    print("Student Added Successfully.")


def display_students():

    cursor.execute("SELECT * FROM students")

    for student in cursor.fetchall():
        print(student)


while True:

    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Exit")

    choice = input("Choice: ")

    match choice:

        case "1":
            add_student()

        case "2":
            display_students()

        case "3":
            connection.close()
            break

        case _:
            print("Invalid Choice")
