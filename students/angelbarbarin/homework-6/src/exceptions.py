"""Domain exceptions for the library management system."""


class LibraryError(Exception):
    """Base class for every library rule violation."""


class BookNotAvailableError(LibraryError):
    """Raised when no copies of a book are available."""


class InvalidReturnError(LibraryError):
    """Raised when returning a copy that was never lent."""
