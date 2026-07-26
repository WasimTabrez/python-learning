from student import Student


class Database:

    def __init__(self):

        self.students = {}

    def add(self, student):

        self.students[student.student_id] = student

    def all(self):

        return [

            student.to_dict()

            for student in self.students.values()

        ]

    def get(self, student_id):

        student = self.students.get(student_id)

        if student:

            return student.to_dict()

        return None

    def update(self, student_id, marks):

        if student_id in self.students:

            self.students[student_id].marks = marks

            return True

        return False

    def delete(self, student_id):

        if student_id in self.students:

            del self.students[student_id]

            return True

        return False
