# Delete Record

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

student_id = int(input("Enter Student ID to Delete: "))

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)

connection.commit()

if cursor.rowcount > 0:
    print("Record Deleted Successfully.")
else:
    print("Student ID Not Found.")

connection.close()
