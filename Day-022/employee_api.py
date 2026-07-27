from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

employees = {}


class Employee(BaseModel):

    id: int
    name: str
    department: str
    salary: float


@app.get("/employees")
def get_employees():

    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    return employees.get(
        employee_id,
        {"error": "Employee Not Found"}
    )


@app.post("/employees")
def add_employee(employee: Employee):

    employees[employee.id] = employee

    return {

        "message": "Employee Added"

    }


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: Employee
):

    employees[employee_id] = employee

    return {

        "message": "Employee Updated"

    }


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    employees.pop(employee_id, None)

    return {

        "message": "Employee Deleted"

    }
