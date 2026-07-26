from employee import Employee
from database import Database
from router import Router


database = Database()

router = Router(database)

database.add(

    Employee(

        1,

        "Wasim",

        "Engineering",

        "Software Engineer",

        120000

    )

)

database.add(

    Employee(

        2,

        "Rahul",

        "QA",

        "QA Engineer",

        80000

    )

)

database.add(

    Employee(

        3,

        "Priya",

        "Engineering",

        "Senior Developer",

        150000

    )

)

print(router.home())

print()

print(router.employees())

print()

print(router.employee(1))

print()

print(

    router.department(

        "Engineering"

    )

)

print()

print(

    router.update_salary(

        2,

        90000

    )

)

print()

print(router.delete(3))

print()

print(router.employees())
