# library_management.py

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def is_available(self):
        """Check if the book is available."""
        return self.copies > 0

    def borrow(self):
        """Borrow a copy of the book."""
        if self.is_available():
            self.copies -= 1
            return True
        return False

    def return_book(self):
        """Return a copy of the book."""
        self.copies += 1


class Library:
    """Represents the library system."""
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, copies):
        """Add a book to the library."""
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)

    def issue_book(self, title):
        """Issue a book to a user."""
        if title in self.books and self.books[title].borrow():
            print(f"Book '{title}' has been issued.")
        else:
            print(f"Book '{title}' is not available.")

    def return_book(self, title):
        """Return a book from a user."""
        if title in self.books:
            self.books[title].return_book()
            print(f"Book '{title}' has been returned.")
        else:
            print(f"Book '{title}' does not belong to this library.")

    def display_books(self):
        """Display all books in the library."""
        print("Books in the library:")
        for title, book in self.books.items():
            print(f"{title} by {book.author} - Copies: {book.copies}")


# Utility functions for interaction
def main():
    library = Library()

    # Add some books
    library.add_book("1984", "George Orwell", 5)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 3)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 2)

    # Display books
    library.display_books()

    # Issue a book
    library.issue_book("1984")

    # Try issuing a book that is out of stock
    library.issue_book("The Great Gatsby")
    library.issue_book("The Great Gatsby")
    library.issue_book("The Great Gatsby")  # No more copies available

    # Return a book
    library.return_book("1984")

    # Display books after transactions
    library.display_books()


if __name__ == "__main__":
    main()
