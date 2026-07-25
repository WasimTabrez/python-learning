# Display Thread Names

import threading
import time


def task():

    print("Current Thread:", threading.current_thread().name)

    time.sleep(2)


thread1 = threading.Thread(target=task, name="DownloadThread")

thread2 = threading.Thread(target=task, name="UploadThread")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main Thread:", threading.current_thread().name)
