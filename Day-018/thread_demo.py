# Create a Simple Thread

import threading
import time


def display_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)


thread = threading.Thread(target=display_numbers)

thread.start()

thread.join()

print("Main Thread Finished")
