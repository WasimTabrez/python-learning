from student import Student
from database import Database
from router import Router


database = Database()

router = Router(database)

database.add(

    Student(

        101,

        "Wasim",

        "Python",

        95

    )

)

database.add(

    Student(

        102,

        "Rahul",

        "AI",

        88

    )

)

print(router.home())

print()

print(router.get_students())

print()

print(router.get_student(101))

print()

print(router.delete_student(102))

print()

print(router.get_students())
