# Create a simple decorator

def decorator(function):

    def wrapper():
        print("Before Function Call")

        function()

        print("After Function Call")

    return wrapper


def greet():
    print("Hello, Wasim!")


greet = decorator(greet)

greet()
