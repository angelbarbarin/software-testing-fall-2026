from book import Book


def test_book_is_created_with_isbn_title_and_author():
    book = Book("0306406152", "Clean Code", "Robert C. Martin")
    assert (book.isbn, book.title, book.author) == (
        "0306406152",
        "Clean Code",
        "Robert C. Martin",
    )


def test_book_starts_with_all_copies_available():
    book = Book("0306406152", "Clean Code", "Robert C. Martin", total_copies=3)
    assert book.available_copies == 3
