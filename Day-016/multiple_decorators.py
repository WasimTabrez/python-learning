# Apply multiple decorators

def stars(function):

    def wrapper(*args, **kwargs):
        print("*" * 30)

        function(*args, **kwargs)

        print("*" * 30)

    return wrapper


def hashes(function):

    def wrapper(*args, **kwargs):
        print("#" * 30)

        function(*args, **kwargs)

        print("#" * 30)

    return wrapper


@stars
@hashes
def message():
    print("Learning Python Decorators")


message()
