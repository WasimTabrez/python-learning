# Nested function example

def outer():

    print("Inside Outer Function")

    def inner():
        print("Inside Inner Function")

    inner()

outer()
