# SQLite Database Operations

import sqlite3

DATABASE_NAME = "students.db"


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE_NAME)

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS students(

            id INTEGER PRIMARY KEY,

            name TEXT NOT NULL,

            age INTEGER,

            course TEXT,

            marks REAL

        )

        """)

        self.connection.commit()

    def add_student(self, student):

        self.cursor.execute("""

        INSERT INTO students

        VALUES (?, ?, ?, ?, ?)

        """, student.to_tuple())

        self.connection.commit()

    def get_all_students(self):

        self.cursor.execute("""

        SELECT *

        FROM students

        ORDER BY id

        """)

        return self.cursor.fetchall()

    def search_student(self, student_id):

        self.cursor.execute("""

        SELECT *

        FROM students

        WHERE id=?

        """, (student_id,))

        return self.cursor.fetchone()

    def update_marks(self, student_id, marks):

        self.cursor.execute("""

        UPDATE students

        SET marks=?

        WHERE id=?

        """, (marks, student_id))

        self.connection.commit()

    def delete_student(self, student_id):

        self.cursor.execute("""

        DELETE FROM students

        WHERE id=?

        """, (student_id,))

        self.connection.commit()

    def close(self):

        self.connection.close()
