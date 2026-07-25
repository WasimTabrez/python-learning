# Insert a Single Record

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
INSERT INTO students
(id, name, age, course, marks)
VALUES
(1, 'Wasim', 25, 'Python', 95.5)
""")

connection.commit()

print("Record inserted successfully.")

connection.close()
