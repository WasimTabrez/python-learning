# Handle SQLite Exceptions

import sqlite3

try:

    connection = sqlite3.connect("student.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM unknown_table")

    records = cursor.fetchall()

    print(records)

except sqlite3.Error as error:

    print("Database Error:")
    print(error)

finally:

    if "connection" in locals():
        connection.close()

    print("Database Closed.")
