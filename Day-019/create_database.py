# Create a SQLite Database

import sqlite3

connection = sqlite3.connect("student.db")

print("Database created successfully.")

connection.close()
