def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a % b


def power(a, b):
    return a ** b
