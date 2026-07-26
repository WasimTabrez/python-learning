import sqlite3

DATABASE = "employees.db"


class EmployeeDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE)

        self.cursor = self.connection.cursor()

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS employees(

            id INTEGER PRIMARY KEY,

            name TEXT,

            department TEXT,

            designation TEXT,

            salary REAL

        )

        """)

        self.connection.commit()

    def add_employee(self, employee):

        self.cursor.execute("""

        INSERT INTO employees

        VALUES (?, ?, ?, ?, ?)

        """, employee.to_tuple())

        self.connection.commit()

    def all_employees(self):

        self.cursor.execute("""

        SELECT *

        FROM employees

        ORDER BY id

        """)

        return self.cursor.fetchall()

    def search(self, employee_id):

        self.cursor.execute("""

        SELECT *

        FROM employees

        WHERE id=?

        """, (employee_id,))

        return self.cursor.fetchone()

    def update_salary(self, employee_id, salary):

        self.cursor.execute("""

        UPDATE employees

        SET salary=?

        WHERE id=?

        """, (salary, employee_id))

        self.connection.commit()

    def delete(self, employee_id):

        self.cursor.execute("""

        DELETE FROM employees

        WHERE id=?

        """, (employee_id,))

        self.connection.commit()

    def total_payroll(self):

        self.cursor.execute("""

        SELECT SUM(salary)

        FROM employees

        """)

        value = self.cursor.fetchone()[0]

        return value or 0

    def average_salary(self):

        self.cursor.execute("""

        SELECT AVG(salary)

        FROM employees

        """)

        value = self.cursor.fetchone()[0]

        return value or 0

    def close(self):

        self.connection.close()
