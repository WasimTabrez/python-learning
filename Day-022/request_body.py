from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class Student(BaseModel):

    id: int

    name: str

    course: str

    marks: int


@app.post("/students")
def create_student(

    student: Student

):

    return {

        "message": "Student Created",

        "student": student

    }
