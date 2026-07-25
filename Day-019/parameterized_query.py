# Parameterized SQL Query

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

student_id = int(input("Enter Student ID: "))

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (student_id,)
)

record = cursor.fetchone()

if record:
    print("\nStudent Details")
    print(record)
else:
    print("Student Not Found.")

connection.close()
