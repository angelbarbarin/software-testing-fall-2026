import pytest

from book import Book
from exceptions import BookNotAvailableError, InvalidReturnError

ISBN = "0306406152"


def make_book(isbn=ISBN, title="Clean Code", author="Robert C. Martin", copies=1):
    return Book(isbn, title, author, total_copies=copies)


def test_book_is_created_with_isbn_title_and_author():
    book = make_book()
    assert (book.isbn, book.title, book.author) == (
        ISBN,
        "Clean Code",
        "Robert C. Martin",
    )


def test_book_starts_with_all_copies_available():
    assert make_book(copies=3).available_copies == 3


def test_book_is_available_when_copies_exist():
    assert make_book(copies=1).is_available() is True


def test_borrow_decreases_available_copies():
    book = make_book(copies=2)
    book.borrow()
    assert book.available_copies == 1


def test_borrow_raises_when_no_copies_available():
    book = make_book(copies=0)
    with pytest.raises(BookNotAvailableError):
        book.borrow()


def test_return_copy_increases_available_copies():
    book = make_book(copies=1)
    book.borrow()
    book.return_copy()
    assert book.available_copies == 1


def test_return_copy_raises_when_all_copies_are_in_library():
    with pytest.raises(InvalidReturnError):
        make_book(copies=1).return_copy()
