import pytest
import textfully
from textfully.exceptions import AuthenticationError


def test_api_key_required():
    """Test that api_key is required for sending messages."""
    textfully.api_key = None
    with pytest.raises(AuthenticationError) as exc_info:
        textfully.send("+16175555555", "Test message")
    assert "No API key provided" in str(exc_info.value)


def test_invalid_api_key(requests_mock):
    """Test that invalid API key raises appropriate error."""
    textfully.api_key = "invalid_key"
    requests_mock.post(
        "https://api.textfully.dev/v1/messages",
        status_code=401,
        json={"error": {"type": "authentication_error", "message": "Invalid API key"}},
    )

    with pytest.raises(AuthenticationError) as exc_info:
        textfully.send("+16175555555", "Test message")
    assert "Invalid API key" in str(exc_info.value)


def test_missing_api_key():
    """Test behavior when API key is missing."""
    textfully.api_key = ""  # Empty string
    with pytest.raises(AuthenticationError) as exc_info:
        textfully.send("+16175555555", "Test message")
    assert "No API key provided" in str(exc_info.value)
