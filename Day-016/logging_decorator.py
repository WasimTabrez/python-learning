# Log function calls

from datetime import datetime


def logger(function):

    def wrapper(*args, **kwargs):

        print(f"[{datetime.now()}] Calling '{function.__name__}'")

        result = function(*args, **kwargs)

        print(f"[{datetime.now()}] '{function.__name__}' Completed\n")

        return result

    return wrapper


@logger
def add(a, b):

    print("Sum =", a + b)


@logger
def greet(name):

    print(f"Hello {name}")


add(10, 20)

greet("Wasim")
