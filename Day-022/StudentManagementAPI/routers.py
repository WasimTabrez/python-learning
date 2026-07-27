from fastapi import APIRouter, HTTPException

from models import Student

import database

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/")
def get_students():

    return database.get_all_students()


@router.get("/{student_id}")
def get_student(student_id: int):

    student = database.get_student(student_id)

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student Not Found"

        )

    return student


@router.post("/")
def add_student(student: Student):

    database.add_student(student)

    return {

        "message": "Student Added",

        "student": student

    }


@router.put("/{student_id}")
def update_student(

    student_id: int,

    student: Student

):

    database.update_student(

        student_id,

        student

    )

    return {

        "message": "Student Updated"

    }


@router.delete("/{student_id}")
def delete_student(student_id: int):

    student = database.delete_student(student_id)

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student Not Found"

        )

    return {

        "message": "Student Deleted"

    }
