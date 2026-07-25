# Backup SQLite Database

import sqlite3

source = sqlite3.connect("student.db")

backup = sqlite3.connect("student_backup.db")

source.backup(backup)

print("Database Backup Completed Successfully.")

backup.close()
source.close()
