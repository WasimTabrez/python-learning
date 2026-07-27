from fastapi import FastAPI

from routers import router

app = FastAPI(

    title="Employee Management API",

    version="1.0.0",

    description="Employee CRUD API using FastAPI"

)


@app.get("/")
def home():

    return {

        "message":

        "Welcome to Employee Management API"

    }


app.include_router(router)
