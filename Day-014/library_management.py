# Library Management System using OOP

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"

        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 35)


class Library:

    def __init__(self):
        self.books = []

    def add_book(self):

        book_id = input("Enter Book ID: ").strip()

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.\n")
                return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        self.books.append(Book(book_id, title, author))

        print("Book added successfully.\n")

    def search_book(self):

        if not self.books:
            print("Library is empty.\n")
            return

        keyword = input("Enter Book ID or Title: ").strip().lower()

        found = False

        for book in self.books:

            if (book.book_id.lower() == keyword or
                    keyword in book.title.lower()):

                book.display()
                found = True

        if not found:
            print("Book not found.\n")

    def borrow_book(self):

        if not self.books:
            print("Library is empty.\n")
            return

        book_id = input("Enter Book ID: ").strip()

        for book in self.books:

            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("Book borrowed successfully.\n")
                else:
                    print("Book is already borrowed.\n")

                return

        print("Book not found.\n")

    def return_book(self):

        if not self.books:
            print("Library is empty.\n")
            return

        book_id = input("Enter Book ID: ").strip()

        for book in self.books:

            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("Book returned successfully.\n")
                else:
                    print("Book is already available.\n")

                return

        print("Book not found.\n")

    def display_books(self):

        if not self.books:
            print("Library is empty.\n")
            return

        print("\n========= Library Books =========\n")

        for book in self.books:
            book.display()

    def count_books(self):
        print(f"Total Books : {len(self.books)}\n")


def menu():

    library = Library()

    while True:

        print("====== Library Management System ======")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Count Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                library.add_book()

            case "2":
                library.search_book()

            case "3":
                library.borrow_book()

            case "4":
                library.return_book()

            case "5":
                library.display_books()

            case "6":
                library.count_books()

            case "7":
                print("Thank you!")
                break

            case _:
                print("Invalid Choice.\n")


menu()
