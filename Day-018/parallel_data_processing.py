# Parallel Data Processing System

from multiprocessing import Pool
import random
import time


def chunk_sum(chunk):
    return sum(chunk)


def chunk_max(chunk):
    return max(chunk)


def chunk_min(chunk):
    return min(chunk)


def split_data(data, num_chunks):

    chunk_size = len(data) // num_chunks

    chunks = []

    start = 0

    for i in range(num_chunks):

        if i == num_chunks - 1:
            chunks.append(data[start:])
        else:
            chunks.append(data[start:start + chunk_size])

        start += chunk_size

    return chunks


def generate_dataset():

    size = int(input("Enter Dataset Size: "))

    data = [random.randint(1, 1000) for _ in range(size)]

    print(f"\nDataset with {size} numbers generated successfully.\n")

    return data


def process_data(data):

    cpu_count = 4

    chunks = split_data(data, cpu_count)

    start = time.perf_counter()

    with Pool(cpu_count) as pool:

        sums = pool.map(chunk_sum, chunks)
        maximums = pool.map(chunk_max, chunks)
        minimums = pool.map(chunk_min, chunks)

    total_sum = sum(sums)
    total_max = max(maximums)
    total_min = min(minimums)
    average = total_sum / len(data)

    end = time.perf_counter()

    print("\n========== Processing Result ==========\n")

    print("Total Numbers :", len(data))
    print("Sum           :", total_sum)
    print("Average       :", round(average, 2))
    print("Maximum       :", total_max)
    print("Minimum       :", total_min)
    print(f"Processing Time : {end-start:.4f} seconds\n")


def menu():

    data = []

    while True:

        print("====== Parallel Data Processing ======")

        print("1. Generate Dataset")
        print("2. Process Dataset")
        print("3. Exit")

        choice = input("Enter Choice: ")

        match choice:

            case "1":
                data = generate_dataset()

            case "2":

                if data:
                    process_data(data)
                else:
                    print("Please generate dataset first.\n")

            case "3":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice.\n")


if __name__ == "__main__":
    menu()
