from fastapi import APIRouter, HTTPException

from models import Employee

import database

router = APIRouter(

    prefix="/employees",

    tags=["Employees"]

)


@router.get("/")
def get_employees():

    return database.get_all()


@router.get("/{employee_id}")
def get_employee(employee_id: int):

    employee = database.get(employee_id)

    if employee is None:

        raise HTTPException(

            status_code=404,

            detail="Employee Not Found"

        )

    return employee


@router.post("/")
def add_employee(employee: Employee):

    database.add(employee)

    return {

        "message": "Employee Added",

        "employee": employee

    }


@router.put("/{employee_id}")
def update_employee(

    employee_id: int,

    employee: Employee

):

    database.update(

        employee_id,

        employee

    )

    return {

        "message": "Employee Updated"

    }


@router.put("/{employee_id}/salary")
def update_salary(

    employee_id: int,

    salary: float

):

    employee = database.update_salary(

        employee_id,

        salary

    )

    if employee is None:

        raise HTTPException(

            status_code=404,

            detail="Employee Not Found"

        )

    return {

        "message": "Salary Updated",

        "employee": employee

    }


@router.get("/department/{department}")
def department(department: str):

    return database.get_by_department(

        department

    )


@router.delete("/{employee_id}")
def delete_employee(employee_id: int):

    employee = database.delete(employee_id)

    if employee is None:

        raise HTTPException(

            status_code=404,

            detail="Employee Not Found"

        )

    return {

        "message": "Employee Deleted"

    }
