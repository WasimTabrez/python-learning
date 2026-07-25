# Student Management System using SQLite

import sqlite3


connection = sqlite3.connect("student_management.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

connection.commit()


def add_student():

    try:

        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        cursor.execute("""
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?)
        """, (student_id, name, age, course, marks))

        connection.commit()

        print("Student Added Successfully.\n")

    except sqlite3.IntegrityError:
        print("Student ID Already Exists.\n")

    except ValueError:
        print("Invalid Input.\n")


def search_student():

    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    record = cursor.fetchone()

    if record:

        print("\nStudent Details")

        print("-" * 50)

        print(f"ID      : {record[0]}")
        print(f"Name    : {record[1]}")
        print(f"Age     : {record[2]}")
        print(f"Course  : {record[3]}")
        print(f"Marks   : {record[4]}")

    else:
        print("Student Not Found.")


def update_student():

    student_id = int(input("Enter Student ID: "))
    marks = float(input("Enter New Marks: "))

    cursor.execute("""
    UPDATE students
    SET marks=?
    WHERE id=?
    """, (marks, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Record Updated Successfully.")
    else:
        print("Student Not Found.")


def delete_student():

    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")


def display_students():

    cursor.execute("SELECT * FROM students ORDER BY id")

    records = cursor.fetchall()

    if not records:
        print("No Records Found.")
        return

    print("\n")

    print("=" * 72)

    print(f"{'ID':<6}{'NAME':<20}{'AGE':<8}{'COURSE':<20}{'MARKS'}")

    print("=" * 72)

    for student in records:

        print(
            f"{student[0]:<6}"
            f"{student[1]:<20}"
            f"{student[2]:<8}"
            f"{student[3]:<20}"
            f"{student[4]}"
        )


def count_students():

    cursor.execute("SELECT COUNT(*) FROM students")

    count = cursor.fetchone()[0]

    print(f"\nTotal Students : {count}")


def menu():

    while True:

        print("\n====== Student Management System ======")

        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Count Students")
        print("7. Exit")

        choice = input("Enter Choice: ")

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
                count_students()

            case "7":

                connection.close()

                print("Thank You!")

                break

            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    menu()
