from fastapi import FastAPI

app = FastAPI(

    title="Student API",

    description="Learning FastAPI",

    version="1.0.0"

)


@app.get("/")
def home():

    return {

        "message": "Welcome"

    }
