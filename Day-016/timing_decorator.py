# Measure execution time

import time


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(f"\nExecution Time : {end - start:.6f} seconds")

        return result

    return wrapper


@timer
def display_numbers():

    for i in range(1, 6):
        print(i)
        time.sleep(0.5)


display_numbers()
