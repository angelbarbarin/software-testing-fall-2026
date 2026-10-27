import pytest

from book import Book
from exceptions import BookNotFoundError, BorrowLimitExceededError, MemberNotFoundError
from library import Library
from member import Member

ISBN = "0306406152"


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(Book(ISBN, "Clean Code", "Robert C. Martin", total_copies=2))
    lib.register_member(Member("M001", "Ana Lopez"))
    return lib


def test_add_book_makes_it_findable_by_isbn():
    library = Library()
    book = Book(ISBN, "Clean Code", "Robert C. Martin")
    library.add_book(book)
    assert library.get_book(ISBN) is book


def test_register_member_makes_it_findable_by_id():
    library = Library()
    member = Member("M001", "Ana Lopez")
    library.register_member(member)
    assert library.get_member("M001") is member


def test_borrow_book_assigns_copy_to_member(library):
    library.borrow_book("M001", ISBN)
    assert library.get_member("M001").borrowed_books == [ISBN]


def test_borrow_book_raises_for_unknown_member(library):
    with pytest.raises(MemberNotFoundError):
        library.borrow_book("M999", ISBN)


def test_borrow_book_raises_for_unknown_isbn(library):
    with pytest.raises(BookNotFoundError):
        library.borrow_book("M001", "9999999999")


def test_borrow_book_keeps_copy_when_member_reached_limit(library):
    library.register_member(Member("M002", "Luis Perez", max_borrow_limit=0))
    with pytest.raises(BorrowLimitExceededError):
        library.borrow_book("M002", ISBN)
    assert library.get_book(ISBN).available_copies == 2
