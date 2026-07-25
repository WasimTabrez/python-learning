# Insert Multiple Records

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

students = [

    (2, "John", 22, "Java", 89),

    (3, "Alice", 21, "C++", 91),

    (4, "David", 23, "Python", 87),

    (5, "Sara", 22, "Data Science", 94)

]

cursor.executemany("""
INSERT INTO students
(id, name, age, course, marks)
VALUES (?, ?, ?, ?, ?)
""", students)

connection.commit()

print("Multiple records inserted successfully.")

connection.close()
