from datetime import date
from decimal import Decimal

ISBN = "0306406152"


def test_loan_is_due_fourteen_days_after_borrowing(library):
    library.borrow_book("M001", ISBN)
    assert library.get_loan("M001", ISBN).due_date == date(2026, 10, 15)


def test_late_fee_is_zero_on_due_date(library, clock):
    library.borrow_book("M001", ISBN)
    clock.advance(14)
    assert library.calculate_late_fee("M001", ISBN) == Decimal("0")
