import pytest
import requests
import textfully
from textfully.exceptions import APIError


def test_invalid_phone_number():
    """Test validation of phone number format."""
    textfully.api_key = "test_key"
    with pytest.raises(ValueError) as exc_info:
        textfully.send("1234567890", "Test message")  # Invalid format
    assert "Invalid phone number format" in str(exc_info.value)


def test_successful_send(mock_requests):
    """Test successful message sending."""
    textfully.api_key = "test_key"
    mock_response = {
        "id": "msg_123",
        "status": "queued",
        "created_at": "2024-03-21T10:00:00Z",
    }
    mock_requests.post("https://api.textfully.dev/v1/messages", json=mock_response)

    response = textfully.send("+16175555555", "Test message")
    assert response["id"] == "msg_123"
    assert response["status"] == "queued"


def test_api_error(mock_requests):
    """Test handling of API errors."""
    textfully.api_key = "test_key"
    error_response = {
        "error": {"type": "rate_limit_error", "message": "Too many requests"}
    }
    mock_requests.post(
        "https://api.textfully.dev/v1/messages", status_code=429, json=error_response
    )

    with pytest.raises(APIError) as exc_info:
        textfully.send("+16175555555", "Test message")
    assert "Too many requests" in str(exc_info.value)


def test_timeout(mock_requests):
    """Test handling of request timeouts."""
    textfully.api_key = "test_key"
    mock_requests.post(
        "https://api.textfully.dev/v1/messages", exc=requests.exceptions.Timeout
    )

    with pytest.raises(APIError) as exc_info:
        textfully.send("+16175555555", "Test message")
    assert "Request timed out" in str(exc_info.value)
