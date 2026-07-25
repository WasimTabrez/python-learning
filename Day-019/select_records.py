# Display All Records

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print("\nStudent Records")

print("-" * 60)

print(f"{'ID':<5}{'Name':<15}{'Age':<8}{'Course':<18}{'Marks'}")

print("-" * 60)

for student in records:

    print(
        f"{student[0]:<5}"
        f"{student[1]:<15}"
        f"{student[2]:<8}"
        f"{student[3]:<18}"
        f"{student[4]}"
    )

connection.close()
