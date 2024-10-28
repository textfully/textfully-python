import pytest
import requests
from textfully import send
from textfully.exceptions import AuthenticationError, APIError


def test_send_auth_error(requests_mock):
    """Test authentication error."""
    requests_mock.post(
        "https://api.textfully.dev/v1/messages",
        status_code=401,
        json={"error": {"type": "authentication_error", "message": "Invalid API key"}},
    )

    with pytest.raises(AuthenticationError) as exc:
        send("+16175555555", "Test message")
    assert "Invalid API key" in str(exc.value)


def test_send_api_error(requests_mock):
    """Test API error."""
    requests_mock.post(
        "https://api.textfully.dev/v1/messages",
        status_code=400,
        json={"error": {"type": "validation_error", "message": "Invalid request"}},
    )

    with pytest.raises(APIError) as exc:
        send("+16175555555", "Test message")
    assert "Invalid request" in str(exc.value)


def test_send_timeout(requests_mock):
    """Test timeout handling."""
    requests_mock.post(
        "https://api.textfully.dev/v1/messages", exc=requests.exceptions.Timeout
    )

    with pytest.raises(APIError) as exc:
        send("+16175555555", "Test message")
    assert "Request timed out" in str(exc.value)


def test_send_network_error(requests_mock):
    """Test network error handling."""
    requests_mock.post(
        "https://api.textfully.dev/v1/messages", exc=requests.exceptions.ConnectionError
    )

    with pytest.raises(APIError) as exc:
        send("+16175555555", "Test message")
    assert "Request failed" in str(exc.value)


def test_send_invalid_json(requests_mock):
    """Test invalid JSON response."""
    requests_mock.post("https://api.textfully.dev/v1/messages", text="invalid json")

    with pytest.raises(APIError) as exc:
        send("+16175555555", "Test message")
    assert "Invalid JSON response" in str(exc.value)


def test_send_empty_response(requests_mock):
    """Test empty response handling."""
    requests_mock.post("https://api.textfully.dev/v1/messages", text="")

    with pytest.raises(APIError) as exc:
        send("+16175555555", "Test message")
    assert "Invalid JSON response" in str(exc.value)
