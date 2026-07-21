# Returning a function from another function

def outer():

    def inner():
        print("Inner function executed.")

    return inner

result = outer()

result()
