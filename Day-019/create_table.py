# Create Student Table

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

connection.commit()

print("Table created successfully.")

connection.close()
