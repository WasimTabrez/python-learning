from response import response


class Router:

    def __init__(self, database):

        self.database = database

    def home(self):

        return response(

            200,

            {

                "message":

                "Welcome to Employee REST API"

            }

        )

    def employees(self):

        return response(

            200,

            self.database.get_all()

        )

    def employee(self, employee_id):

        employee = self.database.get(employee_id)

        if employee:

            return response(

                200,

                employee

            )

        return response(

            404,

            {

                "error":

                "Employee Not Found"

            }

        )

    def update_salary(self, employee_id, salary):

        if self.database.update_salary(

            employee_id,

            salary

        ):

            return response(

                200,

                {

                    "message":

                    "Salary Updated"

                }

            )

        return response(

            404,

            {

                "error":

                "Employee Not Found"

            }

        )

    def department(self, department):

        return response(

            200,

            self.database.by_department(

                department

            )

        )

    def delete(self, employee_id):

        if self.database.delete(employee_id):

            return response(

                200,

                {

                    "message":

                    "Employee Deleted"

                }

            )

        return response(

            404,

            {

                "error":

                    "Employee Not Found"

            }

        )
