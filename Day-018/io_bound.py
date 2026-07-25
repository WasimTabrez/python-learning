# I/O-bound Task using Multithreading

import threading
import time


def download(file_name):

    print(f"Downloading {file_name}...")

    time.sleep(2)

    print(f"{file_name} Downloaded")


files = [
    "Python.pdf",
    "Data.csv",
    "Image.png",
    "Video.mp4"
]

threads = []

start = time.perf_counter()

for file in files:

    thread = threading.Thread(
        target=download,
        args=(file,)
    )

    threads.append(thread)

    thread.start()


for thread in threads:
    thread.join()

end = time.perf_counter()

print(f"\nTotal Time: {end - start:.2f} seconds")
