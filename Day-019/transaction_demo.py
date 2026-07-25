# Demonstrate commit() and rollback()

import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

try:

    cursor.execute("""
    INSERT INTO students
    VALUES
    (6,'Rahul',22,'Python',88)
    """)

    cursor.execute("""
    INSERT INTO students
    VALUES
    (7,'Priya',23,'Java',91)
    """)

    connection.commit()

    print("Transaction Successful.")

except sqlite3.Error as error:

    connection.rollback()

    print("Transaction Failed.")
    print(error)

finally:

    connection.close()
