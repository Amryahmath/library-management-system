import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'
        self.borrow_date = None
        self.return_date = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'available':
                    book.status = 'borrowed'
                    book.borrow_date = datetime.datetime.now()
                    print(f"Book '{book.title}' borrowed successfully!")
                else:
                    print(f"Book '{book.title}' is currently borrowed.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'borrowed':
                    book.status = 'available'
                    book.return_date = datetime.datetime.now()
                    print(f"Book '{book.title}' returned successfully!")
                else:
                    print(f"Book '{book.title}' was not borrowed.")
                return
        print("Book not found.")

    def view_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.status == 'available':
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def view_borrowed_books(self):
        print("Borrowed Books:")
        for book in self.books:
            if book.status == 'borrowed':
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Borrow Date: {book.borrow_date}")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. View Borrowed Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)
        elif choice == '3':
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)
        elif choice == '4':
            library.view_available_books()
        elif choice == '5':
            library.view_borrowed_books()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
