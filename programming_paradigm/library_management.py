class Book:
    def __init__(self, title, author):
        """Initialize a Book with title, author, and set it as available"""
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute (by convention)

    def check_out(self):
        """Mark the book as checked out"""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned"""
        if not self._is_checked_out:
            return False  # Wasn't checked out
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty collection of books"""
        self._books = []  # Private list of books

    def add_book(self, book):
        """Add a book to the library's collection"""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Can only add Book objects to the library")

    def find_book(self, title):
        """Find a book by title (case-insensitive)"""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """Check out a book by title if it's available"""
        book = self.find_book(title)
        if book is None:
            print(f"Book '{title}' not found in the library")
            return False
        if not book.check_out():
            print(f"Book '{title}' is already checked out")
            return False
        return True

    def return_book(self, title):
        """Return a book by title if it was checked out"""
        book = self.find_book(title)
        if book is None:
            print(f"Book '{title}' not found in the library")
            return False
        if not book.return_book():
            print(f"Book '{title}' wasn't checked out")
            return False
        return True

    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        for book in available_books:
            print(book)
