# Menu-driven File Manager

import os
import shutil
from datetime import datetime


def create_file():
    filename = input("Enter File Name: ").strip()

    try:
        with open(filename, "x"):
            pass
        print("File created successfully.\n")

    except FileExistsError:
        print("File already exists.\n")

    except OSError as error:
        print(error)
        print()


def write_file():
    filename = input("Enter File Name: ").strip()

    text = input("Enter Text: ")

    try:
        with open(filename, "w") as file:
            file.write(text)

        print("Data written successfully.\n")

    except Exception as error:
        print(error)
        print()


def read_file():
    filename = input("Enter File Name: ").strip()

    try:
        with open(filename, "r") as file:

            print("\nFile Contents")
            print("-------------")

            print(file.read())
            print()

    except FileNotFoundError:
        print("File not found.\n")

    except IsADirectoryError:
        print("That is a folder, not a file.\n")

    except UnicodeDecodeError:
        print("Cannot read file: not a text file.\n")


def append_file():
    filename = input("Enter File Name: ").strip()

    text = input("Enter Text to Append: ")

    try:
        with open(filename, "a") as file:
            file.write(text + "\n")

        print("Data appended successfully.\n")

    except Exception as error:
        print(error)
        print()


def delete_file():
    filename = input("Enter File Name: ").strip()

    try:
        os.remove(filename)
        print("File deleted successfully.\n")

    except FileNotFoundError:
        print("File not found.\n")

    except IsADirectoryError:
        print("That is a folder, not a file. Use Delete Folder instead.\n")

    except OSError as error:
        print(error)
        print()


def rename_file():
    old_name = input("Enter Existing File Name: ").strip()
    new_name = input("Enter New File Name: ").strip()

    try:
        os.rename(old_name, new_name)
        print("File renamed successfully.\n")

    except FileNotFoundError:
        print("File not found.\n")

    except OSError as error:
        print(error)
        print()


def copy_file():
    source = input("Enter Source File: ").strip()
    destination = input("Enter Destination File: ").strip()

    try:
        shutil.copy(source, destination)
        print("File copied successfully.\n")

    except FileNotFoundError:
        print("Source file not found.\n")

    except shutil.SameFileError:
        print("Source and destination are the same file.\n")

    except OSError as error:
        print(error)
        print()


def file_information():
    filename = input("Enter File Name: ").strip()

    if not os.path.exists(filename):
        print("File not found.\n")
        return

    print("\nFile Information")
    print("----------------")
    print("Name :", filename)
    print("Absolute Path :", os.path.abspath(filename))
    print("Size :", os.path.getsize(filename), "bytes")
    print()


def list_files():

    print("\nFiles in Current Directory")
    print("--------------------------")

    found = False

    for file in os.listdir():

        if os.path.isfile(file):
            found = True
            print(file)

    if not found:
        print("No files found.")

    print()


def search_word():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    word = input("Enter Word to Search: ").strip()

    found = False

    try:
        with open(filename, "r") as file:

            for line_no, line in enumerate(file, start=1):

                if word.lower() in line.lower():
                    found = True
                    print(f"Line {line_no}: {line.strip()}")

    except UnicodeDecodeError:
        print("Cannot read file: not a text file.\n")
        return

    if not found:
        print("Word not found.")

    print()


def replace_word():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    old_word = input("Old Word: ")
    new_word = input("New Word: ")

    try:
        with open(filename, "r") as file:
            text = file.read()

    except UnicodeDecodeError:
        print("Cannot read file: not a text file.\n")
        return

    text = text.replace(old_word, new_word)

    with open(filename, "w") as file:
        file.write(text)

    print("Word replaced successfully.\n")


def count_lines():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    try:
        with open(filename, "r") as file:
            total = sum(1 for _ in file)

    except UnicodeDecodeError:
        print("Cannot read file: not a text file.\n")
        return

    print("Total Lines:", total)
    print()


def count_words():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    try:
        with open(filename, "r") as file:
            words = file.read().split()

    except UnicodeDecodeError:
        print("Cannot read file: not a text file.\n")
        return

    print("Total Words:", len(words))
    print()


def count_characters():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    try:
        with open(filename, "r") as file:
            text = file.read()

    except UnicodeDecodeError:
        print("Cannot read file: not a text file.\n")
        return

    print("Total Characters:", len(text))
    print()


def show_current_directory():

    print("\nCurrent Directory")
    print("-----------------")

    print(os.getcwd())
    print()


def create_folder():

    folder = input("Enter Folder Name: ").strip()

    try:
        os.mkdir(folder)
        print("Folder created successfully.\n")

    except FileExistsError:
        print("Folder already exists.\n")

    except FileNotFoundError:
        print("Parent directory does not exist.\n")


def delete_folder():

    folder = input("Enter Folder Name: ").strip()

    try:
        os.rmdir(folder)
        print("Folder deleted successfully.\n")

    except FileNotFoundError:
        print("Folder not found.\n")

    except NotADirectoryError:
        print("That is a file, not a folder.\n")

    except OSError:
        print("Folder is not empty.\n")


def show_python_files():

    print("\nPython Files")
    print("------------")

    found = False

    for file in os.listdir():

        if file.endswith(".py"):
            found = True
            print(file)

    if not found:
        print("No Python files found.")

    print()


def show_file_size():

    filename = input("Enter File Name: ").strip()

    if os.path.isfile(filename):
        print(f"File Size: {os.path.getsize(filename)} bytes\n")
    else:
        print("File not found.\n")


def show_absolute_path():

    filename = input("Enter File Name: ").strip()

    if os.path.exists(filename):
        print("Absolute Path:")
        print(os.path.abspath(filename))
        print()
    else:
        print("File not found.\n")


def search_by_extension():

    extension = input("Enter Extension (py/txt/json/csv): ").strip().lstrip(".")

    found = False

    print()

    for file in os.listdir():

        if file.endswith("." + extension):
            found = True
            print(file)

    if not found:
        print("No matching files found.")

    print()


def last_modified():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    timestamp = os.path.getmtime(filename)

    print("Last Modified:")
    print(datetime.fromtimestamp(timestamp))
    print()


def rename_folder():

    old = input("Old Folder Name: ").strip()
    new = input("New Folder Name: ").strip()

    try:
        os.rename(old, new)
        print("Folder renamed successfully.\n")

    except FileNotFoundError:
        print("Folder not found.\n")


def copy_folder():

    source = input("Source Folder: ").strip()
    destination = input("Destination Folder: ").strip()

    try:
        shutil.copytree(source, destination)
        print("Folder copied successfully.\n")

    except FileExistsError:
        print("Destination folder already exists.\n")

    except FileNotFoundError:
        print("Source folder not found.\n")

    except NotADirectoryError:
        print("Source is not a folder.\n")


def move_file():

    source = input("Source File: ").strip()
    destination = input("Destination Path: ").strip()

    try:
        shutil.move(source, destination)
        print("File moved successfully.\n")

    except FileNotFoundError:
        print("File not found.\n")

    except shutil.Error as error:
        print(error)
        print()


def hidden_files():

    print("\nHidden Files")
    print("------------")

    found = False

    for file in os.listdir():

        if file.startswith("."):
            found = True
            print(file)

    if not found:
        print("No hidden files found.")

    print()


def largest_file():

    largest = None
    max_size = 0

    for file in os.listdir():

        if os.path.isfile(file):

            size = os.path.getsize(file)

            if size > max_size:
                max_size = size
                largest = file

    if largest:
        print("Largest File :", largest)
        print("Size :", max_size, "bytes\n")
    else:
        print("No files found.\n")


def backup_file():

    filename = input("Enter File Name: ").strip()

    if not os.path.isfile(filename):
        print("File not found.\n")
        return

    backup = filename + ".bak"

    shutil.copy2(filename, backup)

    print(f"Backup created: {backup}\n")


def menu():

    while True:

        print("========== File Manager ==========")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Delete File")
        print("6. Rename File")
        print("7. Copy File")
        print("8. File Information")
        print("9. List Files")
        print("10. Search Word in File")
        print("11. Replace Word in File")
        print("12. Count Lines")
        print("13. Count Words")
        print("14. Count Characters")
        print("15. Show Current Directory")
        print("16. Create Folder")
        print("17. Delete Folder")
        print("18. Show Python Files Only")
        print("19. Show File Size")
        print("20. Show Absolute File Path")
        print("21. Search Files by Extension")
        print("22. View Last Modified Time")
        print("23. Rename Folder")
        print("24. Copy Folder")
        print("25. Move File")
        print("26. Display Hidden Files")
        print("27. Find Largest File")
        print("28. Backup File")
        print("29. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:

            case "1":
                create_file()

            case "2":
                write_file()

            case "3":
                read_file()

            case "4":
                append_file()

            case "5":
                delete_file()

            case "6":
                rename_file()

            case "7":
                copy_file()

            case "8":
                file_information()

            case "9":
                list_files()

            case "10":
                search_word()

            case "11":
                replace_word()

            case "12":
                count_lines()

            case "13":
                count_words()

            case "14":
                count_characters()

            case "15":
                show_current_directory()

            case "16":
                create_folder()

            case "17":
                delete_folder()

            case "18":
                show_python_files()

            case "19":
                show_file_size()

            case "20":
                show_absolute_path()

            case "21":
                search_by_extension()

            case "22":
                last_modified()

            case "23":
                rename_folder()

            case "24":
                copy_folder()

            case "25":
                move_file()

            case "26":
                hidden_files()

            case "27":
                largest_file()

            case "28":
                backup_file()

            case "29":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice.\n")


if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
