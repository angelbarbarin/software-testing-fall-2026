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
