from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):

    id: int
    name: str
    department: str
    salary: float


@app.post("/employee")
def create_employee(employee: Employee):

    return employee
