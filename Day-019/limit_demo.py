# Limit Query Results

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM students
LIMIT 3
""")

records = cursor.fetchall()

print("First Three Records\n")

for student in records:
    print(student)

connection.close()
