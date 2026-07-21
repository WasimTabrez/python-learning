# Decorator with *args and **kwargs

def decorator(function):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = function(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper


@decorator
def add(a, b):
    print(f"Sum = {a + b}")


@decorator
def introduce(name, age):
    print(f"Name : {name}")
    print(f"Age  : {age}")


add(10, 20)

print()

introduce("Wasim", 40)
