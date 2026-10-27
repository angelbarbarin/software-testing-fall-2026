from book import Book
from library import Library

ISBN = "0306406152"


def test_add_book_makes_it_findable_by_isbn():
    library = Library()
    book = Book(ISBN, "Clean Code", "Robert C. Martin")
    library.add_book(book)
    assert library.get_book(ISBN) is book
