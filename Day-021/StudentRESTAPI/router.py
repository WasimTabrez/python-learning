from response import response


class Router:

    def __init__(self, database):

        self.database = database

    def home(self):

        return response(

            200,

            {

                "message":

                "Welcome to Student REST API"

            }

        )

    def get_students(self):

        return response(

            200,

            self.database.all()

        )

    def get_student(self, student_id):

        student = self.database.get(student_id)

        if student:

            return response(

                200,

                student

            )

        return response(

            404,

            {

                "error":

                "Student Not Found"

            }

        )

    def delete_student(self, student_id):

        if self.database.delete(student_id):

            return response(

                200,

                {

                    "message":

                    "Student Deleted"

                }

            )

        return response(

            404,

            {

                "error":

                "Student Not Found"

            }

        )
