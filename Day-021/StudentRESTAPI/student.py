class Student:

    def __init__(self, student_id, name, course, marks):

        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def to_dict(self):

        return {

            "id": self.student_id,
            "name": self.name,
            "course": self.course,
            "marks": self.marks

        }
