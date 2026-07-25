# Demonstrate Process Pool

from multiprocessing import Pool


def square(number):

    return number * number


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=4) as pool:

        result = pool.map(square, numbers)

    print("Squares:", result)
