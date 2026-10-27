"""Library catalog and lending operations."""

from exceptions import (
    AlreadyBorrowedError,
    BookNotFoundError,
    BorrowLimitExceededError,
    MemberNotFoundError,
)


class Library:
    """Coordinates the catalog, the members and their loans."""

    def __init__(self):
        self._books = {}
        self._members = {}

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
        if isbn in member.borrowed_books:
            raise AlreadyBorrowedError(f"{member.name} already has {isbn}")
        if not member.can_borrow():
            raise BorrowLimitExceededError(f"{member.name} reached the borrow limit")
        book.borrow()
        member.add_borrowed_book(isbn)

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
    def _lookup(registry, key, error):
        if key not in registry:
            raise error(f"{key} was not found")
        return registry[key]
