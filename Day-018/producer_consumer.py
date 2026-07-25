# Producer-Consumer Problem

from queue import Queue
import threading
import time
import random

queue = Queue(maxsize=5)


def producer():

    for i in range(10):

        item = random.randint(1, 100)

        queue.put(item)

        print(f"Produced {item}")

        time.sleep(1)


def consumer():

    for _ in range(10):

        item = queue.get()

        print(f"Consumed {item}")

        queue.task_done()

        time.sleep(2)


producer_thread = threading.Thread(target=producer)

consumer_thread = threading.Thread(target=consumer)

producer_thread.start()

consumer_thread.start()

producer_thread.join()

queue.join()

consumer_thread.join()

print("Producer-Consumer Completed")
