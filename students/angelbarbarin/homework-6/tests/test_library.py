import pytest

from book import Book
from exceptions import MemberNotFoundError
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
