import pytest
import textfully
from textfully import send
from textfully.exceptions import AuthenticationError


def test_send_with_missing_api_key():
    """Test sending without API key."""
    textfully.api_key = None  # Override the fixture

    with pytest.raises(AuthenticationError) as exc:
        send("+16178856037", "Test message")
    assert "No API key provided" in str(exc.value)


def test_send_with_invalid_phone(mock_requests):
    """Test sending with invalid phone number."""
    with pytest.raises(ValueError) as exc:
        send("1234567890", "Test message")
    assert "Invalid phone number format" in str(exc.value)
    assert "E.164 format" in str(exc.value)
    mock_requests.post.assert_not_called()


def test_send_with_empty_phone(mock_requests):
    """Test sending with empty phone number."""
    with pytest.raises(ValueError) as exc:
        send("", "Test message")
    assert "Invalid phone number format" in str(exc.value)
    assert "E.164 format" in str(exc.value)
    mock_requests.post.assert_not_called()


def test_send_with_malformed_phone(mock_requests):
    """Test sending with malformed phone numbers."""
    test_cases = [
        "+123",  # Too short
        "+11234567890123456",  # Too long
        "++16178856037",  # Double plus
        "+1617555555a",  # Non-numeric characters
        "+0123456789",  # Starting with 0 after +
    ]

    for phone in test_cases:
        with pytest.raises(ValueError) as exc:
            send(phone, "Test message")
        assert "Invalid phone number format" in str(exc.value)
        assert "E.164 format" in str(exc.value)
        mock_requests.post.assert_not_called()
