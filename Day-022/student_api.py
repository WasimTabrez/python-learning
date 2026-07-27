from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {}


class Student(BaseModel):

    id: int
    name: str
    course: str
    marks: int


@app.get("/students")
def get_students():

    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    return students.get(
        student_id,
        {"error": "Student Not Found"}
    )


@app.post("/students")
def add_student(student: Student):

    students[student.id] = student

    return {

        "message": "Student Added"

    }


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: Student
):

    students[student_id] = student

    return {

        "message": "Student Updated"

    }


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    students.pop(student_id, None)

    return {

        "message": "Student Deleted"

    }
