from models import Employee

employees = {}


def get_all():

    return employees


def get(employee_id: int):

    return employees.get(employee_id)


def add(employee: Employee):

    employees[employee.id] = employee

    return employee


def update(employee_id: int, employee: Employee):

    employees[employee_id] = employee

    return employee


def delete(employee_id: int):

    return employees.pop(employee_id, None)


def get_by_department(department: str):

    return {

        employee_id: employee

        for employee_id, employee

        in employees.items()

        if employee.department.lower()

        == department.lower()

    }


def update_salary(employee_id: int, salary: float):

    employee = employees.get(employee_id)

    if employee:

        employee.salary = salary

        return employee

    return None
