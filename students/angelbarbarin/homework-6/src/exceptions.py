"""Domain exceptions for the library management system."""


class LibraryError(Exception):
    """Base class for every library rule violation."""


class BookNotAvailableError(LibraryError):
    """Raised when no copies of a book are available."""


class InvalidReturnError(LibraryError):
    """Raised when returning a copy that was never lent."""


class BorrowLimitExceededError(LibraryError):
    """Raised when a member already has the maximum number of books."""


class MemberNotFoundError(LibraryError):
    """Raised when a member id is not registered."""
