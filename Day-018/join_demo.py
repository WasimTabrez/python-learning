# Demonstrate join()

import threading
import time


def worker():

    print("Worker Started")

    time.sleep(3)

    print("Worker Finished")


thread = threading.Thread(target=worker)

thread.start()

print("Waiting for Worker...")

thread.join()

print("Main Thread Continues")
