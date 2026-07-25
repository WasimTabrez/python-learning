# Count Total Records

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")

count = cursor.fetchone()[0]

print(f"Total Students: {count}")

connection.close()
