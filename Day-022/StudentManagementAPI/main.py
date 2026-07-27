from fastapi import FastAPI

from routers import router

app = FastAPI(

    title="Student Management API",

    version="1.0",

    description="FastAPI CRUD Example"

)


@app.get("/")
def home():

    return {

        "message":

        "Welcome to Student Management API"

    }


app.include_router(router)
