# Filter Records using WHERE

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

course = input("Enter Course Name: ")

cursor.execute(
    "SELECT * FROM students WHERE course = ?",
    (course,)
)

records = cursor.fetchall()

if records:

    print("\nMatching Records\n")

    for student in records:
        print(student)

else:
    print("No Records Found.")

connection.close()
