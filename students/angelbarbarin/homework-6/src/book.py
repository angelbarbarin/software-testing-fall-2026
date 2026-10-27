"""Book entity of the library catalog."""

from exceptions import BookNotAvailableError, InvalidReturnError


class Book:
    """A title in the catalog with a number of physical copies."""

    def __init__(self, isbn, title, author, total_copies=1):
        isbn = isbn.replace("-", "")
        if not (isbn.isdigit() and len(isbn) in (10, 13)):
            raise ValueError("ISBN must have 10 or 13 digits")
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
        if self.available_copies >= self.total_copies:
            raise InvalidReturnError(f"Every copy of {self.isbn} is already on the shelf")
        self.available_copies += 1
