# Simple caching decorator

def cache(function):

    memory = {}

    def wrapper(number):

        if number in memory:
            print("Returning Cached Result")
            return memory[number]

        result = function(number)

        memory[number] = result

        return result

    return wrapper


@cache
def square(number):

    print("Calculating...")

    return number * number


print(square(10))

print(square(10))

print(square(20))
