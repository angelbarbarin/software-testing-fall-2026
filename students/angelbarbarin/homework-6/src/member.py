"""Library member."""

from exceptions import BorrowLimitExceededError, InvalidReturnError


class Member:
    """A registered person who can borrow books."""

    def __init__(self, member_id, name, max_borrow_limit=3):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.max_borrow_limit = max_borrow_limit

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_borrow_limit

    def add_borrowed_book(self, isbn):
        if not self.can_borrow():
            raise BorrowLimitExceededError(f"{self.name} reached the borrow limit")
        self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            raise InvalidReturnError(f"{self.name} did not borrow {isbn}")
        self.borrowed_books.remove(isbn)
