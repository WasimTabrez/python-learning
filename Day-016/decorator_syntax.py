# Use the @ decorator syntax

def decorator(function):

    def wrapper():
        print("**************")

        function()

        print("**************")

    return wrapper


@decorator
def welcome():
    print("Welcome to Python Decorators")


welcome()
