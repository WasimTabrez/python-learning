from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return {

        "message": "Open Swagger"

    }

"""
Swagger URL

http://127.0.0.1:8000/docs
"""
