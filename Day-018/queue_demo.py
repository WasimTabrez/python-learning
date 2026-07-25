# Thread-safe Communication using Queue

from queue import Queue
import threading

queue = Queue()


def producer():

    for i in range(1, 6):

        print("Produced:", i)

        queue.put(i)


def consumer():

    for _ in range(5):

        item = queue.get()

        print("Consumed:", item)

        queue.task_done()


producer_thread = threading.Thread(target=producer)

consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()

queue.join()

consumer_thread.join()

print("Completed")
