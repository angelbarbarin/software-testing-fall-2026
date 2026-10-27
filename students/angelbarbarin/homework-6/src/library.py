"""Library catalog and lending operations."""

from exceptions import BookNotFoundError, MemberNotFoundError


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
        book.borrow()
        member.add_borrowed_book(isbn)

    @staticmethod
    def _lookup(registry, key, error):
        if key not in registry:
            raise error(f"{key} was not found")
        return registry[key]
