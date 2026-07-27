from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/students",
    tags=["Students"]
)
def students():

    return {

        "message": "Student List"

    }


@app.get(
    "/employees",
    tags=["Employees"]
)
def employees():

    return {

        "message": "Employee List"

    }
