# Input Validation

import re


def validate_name(name):

    pattern = r"^[A-Za-z ]+$"

    return bool(re.fullmatch(pattern, name))


def validate_age(age):

    return 18 <= age <= 100


def validate_marks(marks):

    return 0 <= marks <= 100


def validate_course(course):

    pattern = r"^[A-Za-z0-9 +#.-]+$"

    return bool(re.fullmatch(pattern, course))


def validate_student_id(student_id):

    return student_id > 0
