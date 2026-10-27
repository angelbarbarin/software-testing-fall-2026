from datetime import date, timedelta

import pytest


class FakeClock:
    """Controllable replacement for date.today so tests never wait for real days."""

    def __init__(self, today):
        self.today = today

    def __call__(self):
        return self.today

    def advance(self, days):
        self.today += timedelta(days=days)


@pytest.fixture
def clock():
    return FakeClock(date(2026, 10, 1))
