from pydantic import BaseModel, Field


class Student(BaseModel):

    id: int

    name: str = Field(
        min_length=3,
        max_length=50
    )

    course: str

    marks: int = Field(
        ge=0,
        le=100
    )
