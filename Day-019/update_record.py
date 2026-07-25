# Update Existing Record

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

student_id = int(input("Enter Student ID: "))
new_marks = float(input("Enter New Marks: "))

cursor.execute(
    """
    UPDATE students
    SET marks = ?
    WHERE id = ?
    """,
    (new_marks, student_id)
)

connection.commit()

if cursor.rowcount > 0:
    print("Record Updated Successfully.")
else:
    print("Student ID Not Found.")

connection.close()
