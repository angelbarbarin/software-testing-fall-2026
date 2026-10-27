from datetime import date

import pytest

from book import Book
from library import Library
from member import Member

ISBN = "0306406152"


@pytest.fixture
def library(clock):
    lib = Library(clock=clock)
    lib.add_book(Book(ISBN, "Clean Code", "Robert C. Martin"))
    lib.register_member(Member("M001", "Ana Lopez"))
    return lib


def test_loan_is_due_fourteen_days_after_borrowing(library):
    library.borrow_book("M001", ISBN)
    assert library.get_loan("M001", ISBN).due_date == date(2026, 10, 15)
