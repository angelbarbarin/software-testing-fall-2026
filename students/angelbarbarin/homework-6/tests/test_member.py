import pytest

from exceptions import BorrowLimitExceededError
from member import Member


def test_member_is_created_without_borrowed_books():
    member = Member("M001", "Ana Lopez")
    assert (member.member_id, member.name, member.borrowed_books) == (
        "M001",
        "Ana Lopez",
        [],
    )


def test_member_has_default_borrow_limit_of_three():
    assert Member("M001", "Ana Lopez").max_borrow_limit == 3


def test_member_can_borrow_when_under_limit():
    assert Member("M001", "Ana Lopez").can_borrow() is True


def test_add_borrowed_book_records_isbn():
    member = Member("M001", "Ana Lopez")
    member.add_borrowed_book("0306406152")
    assert member.borrowed_books == ["0306406152"]


def test_add_borrowed_book_raises_when_limit_reached():
    member = Member("M001", "Ana Lopez", max_borrow_limit=1)
    member.add_borrowed_book("0306406152")
    with pytest.raises(BorrowLimitExceededError):
        member.add_borrowed_book("9780132350884")
