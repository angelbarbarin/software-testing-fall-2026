from datetime import date
from decimal import Decimal

from member import Member, MemberCategory

ISBN = "0306406152"


def test_loan_is_due_fourteen_days_after_borrowing(library):
    library.borrow_book("M001", ISBN)
    assert library.get_loan("M001", ISBN).due_date == date(2026, 10, 15)


def test_late_fee_is_zero_on_due_date(library, clock):
    library.borrow_book("M001", ISBN)
    clock.advance(14)
    assert library.calculate_late_fee("M001", ISBN) == Decimal("0")


def test_late_fee_is_one_dollar_per_overdue_day(library, clock):
    library.borrow_book("M001", ISBN)
    clock.advance(17)
    assert library.calculate_late_fee("M001", ISBN) == Decimal("3.00")


def test_late_fee_uses_member_category_rate(library, clock):
    faculty = Member("F001", "Dra. Ruiz", category=MemberCategory.FACULTY)
    library.register_member(faculty)
    library.borrow_book("F001", ISBN)
    clock.advance(18)
    assert library.calculate_late_fee("F001", ISBN) == Decimal("2.00")
