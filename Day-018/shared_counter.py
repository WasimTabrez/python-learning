# Shared Counter using Lock

import threading

counter = 0

lock = threading.Lock()


def increment():

    global counter

    for _ in range(100000):

        with lock:
            counter += 1


threads = []

for _ in range(5):

    thread = threading.Thread(target=increment)

    threads.append(thread)

    thread.start()


for thread in threads:
    thread.join()


print("Final Counter =", counter)
