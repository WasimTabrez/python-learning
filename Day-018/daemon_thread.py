# Demonstrate Daemon Thread

import threading
import time


def background_task():

    while True:
        print("Background Task Running...")
        time.sleep(1)


daemon = threading.Thread(target=background_task)

daemon.daemon = True

daemon.start()

time.sleep(5)

print("Main Thread Exiting")
