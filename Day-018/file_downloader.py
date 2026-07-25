# Simulate Concurrent File Downloads

import threading
import time
import random


def download(file_name):

    print(f"Downloading {file_name}...")

    download_time = random.randint(2, 5)

    time.sleep(download_time)

    print(f"{file_name} Downloaded in {download_time} seconds")


files = [

    "Python.pdf",

    "MachineLearning.pdf",

    "Image.png",

    "Video.mp4",

    "Dataset.csv"

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

print(f"\nTotal Time = {end-start:.2f} seconds")
