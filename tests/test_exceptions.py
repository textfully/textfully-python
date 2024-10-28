from textfully.exceptions import AuthenticationError, APIError, TextfullyError


def test_auth_error_inheritance():
    """Test AuthenticationError inheritance."""
    err = AuthenticationError("Test error")
    assert isinstance(err, TextfullyError)
    assert str(err) == "Test error"


def test_api_error_inheritance():
    """Test APIError inheritance."""
    err = APIError("Test error")
    assert isinstance(err, TextfullyError)
    assert str(err) == "Test error"


def test_base_error():
    """Test TextfullyError base class."""
    err = TextfullyError("Test error")
    assert str(err) == "Test error"
