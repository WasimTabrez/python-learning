from fastapi import FastAPI

app = FastAPI()


@app.post("/students")
def add_student():

    return {

        "message": "Student Added Successfully"

    }
