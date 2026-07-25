# CPU-bound Task using Multiprocessing

from multiprocessing import Pool
import time


def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


if __name__ == "__main__":

    numbers = [5000, 5500, 6000, 6500]

    start = time.perf_counter()

    with Pool() as pool:

        pool.map(factorial, numbers)

    end = time.perf_counter()

    print(f"Processing Time: {end - start:.2f} seconds")
