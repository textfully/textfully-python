class TextfullyError(Exception):
    """Base exception for Textfully SDK errors"""

    pass


class AuthenticationError(TextfullyError):
    """Raised when there are authentication issues"""

    pass


class APIError(TextfullyError):
    """Raised when the API returns an error"""

    pass
