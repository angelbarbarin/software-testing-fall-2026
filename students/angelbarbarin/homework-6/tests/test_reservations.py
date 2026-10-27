import pytest

from book import Book
from library import Library
from member import Member

ISBN = "0306406152"


@pytest.fixture
def busy_library(clock):
    library = Library(clock=clock)
    library.add_book(Book(ISBN, "Clean Code", "Robert C. Martin"))
    for member_id in ("M001", "M002", "M003"):
        library.register_member(Member(member_id, f"Member {member_id}"))
    library.borrow_book("M001", ISBN)
    return library


def test_reservations_are_kept_in_fifo_order(busy_library):
    busy_library.reserve_book("M002", ISBN)
    busy_library.reserve_book("M003", ISBN)
    assert busy_library.reservations_for(ISBN) == ["M002", "M003"]
