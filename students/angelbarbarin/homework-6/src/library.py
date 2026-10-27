"""Library catalog and lending operations."""

from datetime import date
from decimal import Decimal

from exceptions import (
    AlreadyBorrowedError,
    BookNotFoundError,
    BorrowLimitExceededError,
    MemberNotFoundError,
)
from loan import Loan


class Library:
    """Coordinates the catalog, the members and their loans."""

    def __init__(self, clock=date.today):
        self._books = {}
        self._members = {}
        self._loans = {}
        self._clock = clock

    def add_book(self, book):
        self._books[book.isbn] = book

    def get_book(self, isbn):
        return self._lookup(self._books, isbn, BookNotFoundError)

    def register_member(self, member):
        self._members[member.member_id] = member

    def get_member(self, member_id):
        return self._lookup(self._members, member_id, MemberNotFoundError)

    def borrow_book(self, member_id, isbn):
        book = self.get_book(isbn)
        member = self.get_member(member_id)
        self._ensure_can_borrow(member, isbn)
        book.borrow()
        member.add_borrowed_book(isbn)
        self._loans[(member_id, isbn)] = Loan(member_id, isbn, self._clock())

    def get_loan(self, member_id, isbn):
        return self._loans[(member_id, isbn)]

    def calculate_late_fee(self, member_id, isbn):
        return Decimal("0")

    def return_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        member.return_book(isbn)
        book.return_copy()

    def search_by_title(self, title):
        return self._search("title", title)

    def search_by_author(self, author):
        return self._search("author", author)

    def get_available_books(self):
        return [book for book in self._books.values() if book.is_available()]

    def _search(self, field, term):
        term = term.lower()
        return [b for b in self._books.values() if term in getattr(b, field).lower()]

    @staticmethod
    def _ensure_can_borrow(member, isbn):
        if isbn in member.borrowed_books:
            raise AlreadyBorrowedError(f"{member.name} already has {isbn}")
        if not member.can_borrow():
            raise BorrowLimitExceededError(f"{member.name} reached the borrow limit")

    @staticmethod
    def _lookup(registry, key, error):
        if key not in registry:
            raise error(f"{key} was not found")
        return registry[key]
