"""Library catalog and lending operations."""

from exceptions import MemberNotFoundError


class Library:
    """Coordinates the catalog, the members and their loans."""

    def __init__(self):
        self._books = {}
        self._members = {}

    def add_book(self, book):
        self._books[book.isbn] = book

    def get_book(self, isbn):
        return self._books[isbn]

    def register_member(self, member):
        self._members[member.member_id] = member

    def get_member(self, member_id):
        if member_id not in self._members:
            raise MemberNotFoundError(f"Member {member_id} is not registered")
        return self._members[member_id]

    def borrow_book(self, member_id, isbn):
        book = self.get_book(isbn)
        member = self.get_member(member_id)
        book.borrow()
        member.add_borrowed_book(isbn)
