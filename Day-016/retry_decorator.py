# Retry a function on failure

import time


def retry(max_attempts):

    def decorator(function):

        def wrapper(*args, **kwargs):

            attempts = 0

            while attempts < max_attempts:

                try:
                    return function(*args, **kwargs)

                except Exception as error:

                    attempts += 1

                    print(f"Attempt {attempts} Failed -> {error}")

                    time.sleep(1)

            print("Maximum retry attempts reached.")

        return wrapper

    return decorator


counter = 0


@retry(3)
def connect():

    global counter

    counter += 1

    print("Connecting...")

    if counter < 3:
        raise Exception("Server Busy")

    print("Connected Successfully")


connect()
