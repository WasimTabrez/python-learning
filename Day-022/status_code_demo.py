from fastapi import FastAPI
from fastapi import status

app = FastAPI()


@app.post(
    "/student",
    status_code=status.HTTP_201_CREATED
)
def add_student():

    return {

        "message": "Student Created"

    }
