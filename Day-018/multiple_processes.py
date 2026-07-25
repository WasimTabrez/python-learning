# Run Multiple Processes

from multiprocessing import Process
import time


def task(name):

    for i in range(5):

        print(f"{name}: {i + 1}")

        time.sleep(1)


if __name__ == "__main__":

    process1 = Process(target=task, args=("Process-1",))
    process2 = Process(target=task, args=("Process-2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All Processes Completed")
