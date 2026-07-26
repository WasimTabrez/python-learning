import re


def validate_name(name):

    return bool(re.fullmatch(r"[A-Za-z ]+", name))


def validate_salary(salary):

    return salary >= 0


def validate_department(department):

    return len(department) > 0


def validate_designation(designation):

    return len(designation) > 0
