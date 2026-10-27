from member import Member


def test_member_is_created_without_borrowed_books():
    member = Member("M001", "Ana Lopez")
    assert (member.member_id, member.name, member.borrowed_books) == (
        "M001",
        "Ana Lopez",
        [],
    )
