from book import Book
from library import Library
from member import Member

ISBN = "0306406152"


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
