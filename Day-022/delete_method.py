from fastapi import FastAPI

app = FastAPI()


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    return {

        "message": "Student Deleted",

        "student_id": student_id

    }
