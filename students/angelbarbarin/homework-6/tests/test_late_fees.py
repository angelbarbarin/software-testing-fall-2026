from datetime import date

ISBN = "0306406152"


def test_loan_is_due_fourteen_days_after_borrowing(library):
    library.borrow_book("M001", ISBN)
    assert library.get_loan("M001", ISBN).due_date == date(2026, 10, 15)
