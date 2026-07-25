# Demonstrate Semaphore

import threading
import time

semaphore = threading.Semaphore(2)


def worker(name):

    with semaphore:

        print(f"{name} started")

        time.sleep(3)

        print(f"{name} finished")


threads = []

for i in range(5):

    thread = threading.Thread(
        target=worker,
        args=(f"Thread-{i+1}",)
    )

    threads.append(thread)

    thread.start()


for thread in threads:
    thread.join()

print("All Threads Completed")
