from fastapi import FastAPI

app = FastAPI()


@app.put("/students/{student_id}")
def update_student(student_id: int):

    return {

        "message": "Student Updated",

        "student_id": student_id

    }
