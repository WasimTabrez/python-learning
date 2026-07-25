# Compare Threads and Processes

import threading
import multiprocessing
import time


def task(name):

    for i in range(5):
        print(f"{name}: {i + 1}")
        time.sleep(1)


if __name__ == "__main__":

    print("========== Thread Example ==========")

    start = time.perf_counter()

    thread1 = threading.Thread(target=task, args=("Thread-1",))
    thread2 = threading.Thread(target=task, args=("Thread-2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end = time.perf_counter()

    print(f"Thread Time: {end-start:.2f} seconds")

    print("\n========== Process Example ==========")

    start = time.perf_counter()

    process1 = multiprocessing.Process(target=task, args=("Process-1",))
    process2 = multiprocessing.Process(target=task, args=("Process-2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.perf_counter()

    print(f"Process Time: {end-start:.2f} seconds")
