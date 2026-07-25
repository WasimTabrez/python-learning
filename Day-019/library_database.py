# Library Management Database

import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    available TEXT
)
""")

connection.commit()


def add_book():

    book_id = int(input("Book ID: "))
    title = input("Book Title: ")
    author = input("Author: ")

    cursor.execute(
        "INSERT INTO books VALUES (?, ?, ?, ?)",
        (book_id, title, author, "Yes")
    )

    connection.commit()

    print("Book Added Successfully.")


def display_books():

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    for book in books:
        print(book)


while True:

    print("\n====== Library Database ======")
    print("1.Add Book")
    print("2.Display Books")
    print("3.Exit")

    choice = input("Choice: ")

    match choice:

        case "1":
            add_book()

        case "2":
            display_books()

        case "3":
            connection.close()
            break

        case _:
            print("Invalid Choice")
