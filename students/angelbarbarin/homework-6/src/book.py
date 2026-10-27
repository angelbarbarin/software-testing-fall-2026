"""Book entity of the library catalog."""


class BookNotAvailableError(Exception):
    """Raised when no copies of a book are available."""


class Book:
    """A title in the catalog with a number of physical copies."""

    def __init__(self, isbn, title, author, total_copies=1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        return self.available_copies > 0

    def borrow(self):
        if not self.is_available():
            raise BookNotAvailableError(f"No copies of {self.isbn} are available")
        self.available_copies -= 1

    def return_copy(self):
        self.available_copies += 1
