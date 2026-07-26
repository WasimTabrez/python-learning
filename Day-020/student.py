# Student Class

class Student:

    def __init__(self, student_id, name, age, course, marks):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_tuple(self):

        return (
            self.student_id,
            self.name,
            self.age,
            self.course,
            self.marks
        )

    def __str__(self):

        return (
            f"ID      : {self.student_id}\n"
            f"Name    : {self.name}\n"
            f"Age     : {self.age}\n"
            f"Course  : {self.course}\n"
            f"Marks   : {self.marks}"
        )
