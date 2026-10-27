"""Library member."""

from decimal import Decimal
from enum import Enum

from exceptions import BorrowLimitExceededError, InvalidReturnError


class MemberCategory(Enum):
    """Kinds of members with different lending rules."""

    STUDENT = "student"
    FACULTY = "faculty"
    PUBLIC = "public"


BORROW_LIMITS = {
    MemberCategory.STUDENT: 3,
    MemberCategory.FACULTY: 5,
    MemberCategory.PUBLIC: 2,
}

DAILY_LATE_FEES = {
    MemberCategory.STUDENT: Decimal("1.00"),
    MemberCategory.FACULTY: Decimal("0.50"),
    MemberCategory.PUBLIC: Decimal("1.50"),
}


class Member:
    """A registered person who can borrow books."""

    def __init__(
        self, member_id, name, max_borrow_limit=None, category=MemberCategory.STUDENT
    ):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.category = category
        if max_borrow_limit is None:
            max_borrow_limit = BORROW_LIMITS[category]
        self.max_borrow_limit = max_borrow_limit

    @property
    def daily_late_fee(self):
        return DAILY_LATE_FEES[self.category]

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
