# Log File Analyzer using Generators

import os


def read_log_file(filename):
    """Generator to read log file line by line."""

    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


def count_total_lines(filename):
    count = 0

    for _ in read_log_file(filename):
        count += 1

    print(f"\nTotal Lines : {count}\n")


def count_log_level(filename, level):
    count = 0

    for line in read_log_file(filename):
        if level.upper() in line.upper():
            count += 1

    print(f"\n{level.upper()} Entries : {count}\n")


def search_keyword(filename):
    keyword = input("Enter keyword to search: ").strip()

    found = False

    print()

    for line in read_log_file(filename):
        if keyword.lower() in line.lower():
            print(line)
            found = True

    if not found:
        print("No matching log entries found.")

    print()


def display_logs(filename):

    print()

    for line in read_log_file(filename):
        print(line)

    print()


def menu():

    filename = "sample_log.txt"

    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return

    while True:

        print("====== Log File Analyzer ======")
        print("1. Display Log File")
        print("2. Count Total Lines")
        print("3. Count ERROR Entries")
        print("4. Count WARNING Entries")
        print("5. Count INFO Entries")
        print("6. Search Log Entries")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                display_logs(filename)

            case "2":
                count_total_lines(filename)

            case "3":
                count_log_level(filename, "ERROR")

            case "4":
                count_log_level(filename, "WARNING")

            case "5":
                count_log_level(filename, "INFO")

            case "6":
                search_keyword(filename)

            case "7":
                print("Thank you!")
                break

            case _:
                print("Invalid Choice.\n")


menu()
