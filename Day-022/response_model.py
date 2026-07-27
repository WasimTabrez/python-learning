from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):

    id: int
    name: str
    course: str


@app.get(
    "/student",
    response_model=Student
)
def get_student():

    return {

        "id": 101,
        "name": "Wasim",
        "course": "Python"

    }
