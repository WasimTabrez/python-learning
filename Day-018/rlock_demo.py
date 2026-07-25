# Demonstrate RLock

import threading

lock = threading.RLock()


def outer():

    with lock:

        print("Outer Function")

        inner()


def inner():

    with lock:

        print("Inner Function")


thread = threading.Thread(target=outer)

thread.start()

thread.join()
