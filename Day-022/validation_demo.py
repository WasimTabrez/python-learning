from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):

    id: int

    name: str = Field(
        min_length=3,
        max_length=30
    )

    marks: int = Field(
        ge=0,
        le=100
    )


@app.post("/student")
def create_student(student: Student):

    return student
