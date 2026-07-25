# Sort Records using ORDER BY

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM students
ORDER BY marks DESC
""")

records = cursor.fetchall()

print("\nStudents Sorted by Marks\n")

for student in records:
    print(student)

connection.close()
