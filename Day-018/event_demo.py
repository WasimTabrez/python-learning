# Synchronize using Event

import threading
import time

event = threading.Event()


def waiter():

    print("Waiting for Event...")

    event.wait()

    print("Event Received")


def sender():

    time.sleep(3)

    print("Setting Event")

    event.set()


thread1 = threading.Thread(target=waiter)

thread2 = threading.Thread(target=sender)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
