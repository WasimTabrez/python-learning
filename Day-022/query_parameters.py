from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
def search_student(

    course: str,

    marks: int

):

    return {

        "course": course,

        "marks": marks

    }
