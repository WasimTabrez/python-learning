# Concurrent File Downloader (Simulation)

import threading
import time
import random

download_lock = threading.Lock()


def download_file(file_name):

    total_steps = 10

    print(f"\nStarting download: {file_name}")

    for step in range(1, total_steps + 1):

        time.sleep(random.uniform(0.2, 0.5))

        progress = step * 10

        with download_lock:
            print(f"{file_name:<20} {progress}%")

    with download_lock:
        print(f"{file_name} Download Completed.\n")


def start_download():

    files = []

    count = int(input("How many files do you want to download? "))

    for i in range(count):
        file_name = input(f"Enter File {i+1} Name: ")
        files.append(file_name)

    threads = []

    start = time.perf_counter()

    print("\nStarting Downloads...\n")

    for file in files:

        thread = threading.Thread(
            target=download_file,
            args=(file,)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()

    print("=" * 45)
    print("All Downloads Completed Successfully.")
    print(f"Total Time : {end-start:.2f} seconds")
    print("=" * 45)


def menu():

    while True:

        print("\n====== Concurrent File Downloader ======")

        print("1. Download Files")
        print("2. Exit")

        choice = input("Enter Choice: ")

        match choice:

            case "1":
                start_download()

            case "2":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    menu()
