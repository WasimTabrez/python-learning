# Create a Simple Process

from multiprocessing import Process
import time


def worker():

    for i in range(1, 6):

        print(f"Worker Process: {i}")

        time.sleep(1)


if __name__ == "__main__":

    process = Process(target=worker)

    process.start()

    process.join()

    print("Main Process Finished")
