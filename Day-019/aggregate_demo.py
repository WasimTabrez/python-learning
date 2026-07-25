# Demonstrate SQL Aggregate Functions

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
SELECT
    COUNT(*),
    SUM(marks),
    AVG(marks),
    MAX(marks),
    MIN(marks)
FROM students
""")

result = cursor.fetchone()

print("\nStudent Statistics\n")

print(f"Total Students : {result[0]}")
print(f"Total Marks    : {result[1]}")
print(f"Average Marks  : {result[2]:.2f}")
print(f"Highest Marks  : {result[3]}")
print(f"Lowest Marks   : {result[4]}")

connection.close()
