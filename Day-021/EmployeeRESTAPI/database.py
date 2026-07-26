from employee import Employee


class Database:

    def __init__(self):

        self.employees = {}

    def add(self, employee):

        self.employees[employee.employee_id] = employee

    def get_all(self):

        return [

            employee.to_dict()

            for employee in self.employees.values()

        ]

    def get(self, employee_id):

        employee = self.employees.get(employee_id)

        if employee:

            return employee.to_dict()

        return None

    def update_salary(self, employee_id, salary):

        employee = self.employees.get(employee_id)

        if employee:

            employee.salary = salary

            return True

        return False

    def delete(self, employee_id):

        if employee_id in self.employees:

            del self.employees[employee_id]

            return True

        return False

    def by_department(self, department):

        return [

            employee.to_dict()

            for employee in self.employees.values()

            if employee.department.lower() == department.lower()

        ]
