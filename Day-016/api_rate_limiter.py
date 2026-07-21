# API Rate Limiter using Decorators

import time

LIMIT = 5
WINDOW = 30

calls = []


def rate_limit(function):

    def wrapper(*args, **kwargs):

        global calls

        current = time.time()

        calls = [call for call in calls if current - call < WINDOW]

        if len(calls) >= LIMIT:

            remaining = WINDOW - int(current - calls[0])

            print(f"\nRate Limit Exceeded.")
            print(f"Try again after {remaining} seconds.\n")

            return

        calls.append(current)

        print(f"Remaining Requests : {LIMIT-len(calls)}")

        return function(*args, **kwargs)

    return wrapper


@rate_limit
def access_api():

    print("API Request Successful.\n")


def menu():

    while True:

        print("====== API Rate Limiter ======")

        print("1. Access API")
        print("2. Wait 10 Seconds")
        print("3. Exit")

        choice = input("Enter Choice : ")

        match choice:

            case "1":

                access_api()

            case "2":

                print("Waiting...\n")

                time.sleep(10)

            case "3":

                print("Thank You!")

                break

            case _:

                print("Invalid Choice\n")


menu()
