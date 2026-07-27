from models import Student

students = {}


def get_all_students():

    return students


def get_student(student_id: int):

    return students.get(student_id)


def add_student(student: Student):

    students[student.id] = student

    return student


def update_student(student_id: int, student: Student):

    students[student_id] = student

    return student


def delete_student(student_id: int):

    return students.pop(student_id, None)
