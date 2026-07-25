# Synchronize Threads using Lock

import threading
import time

counter = 0

lock = threading.Lock()


def increment():

    global counter

    for _ in range(100000):

        lock.acquire()

        counter += 1

        lock.release()


thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final Counter:", counter)
