import pytest
import textfully
from unittest.mock import patch, Mock


@pytest.fixture(autouse=True)
def setup_api_key():
    """Fixture to set up API key before each test."""
    textfully.api_key = "test_key"
    yield
    textfully.api_key = None


@pytest.fixture
def mock_success_response(requests_mock):
    """Fixture for successful API response."""
    requests_mock.post(
        "https://api.textfully.dev/v1/messages",
        json={"id": "msg_123", "status": "sent", "created_at": "2024-03-21T12:00:00Z"},
    )
    return requests_mock


@pytest.fixture
def mock_requests():
    """Fixture for simulating API calls."""
    with patch("textfully.requests") as mock:
        # Set up mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.ok = True
        mock_response.json.return_value = {
            "id": "msg_123",
            "status": "sent",
            "created_at": "2024-03-21T12:00:00Z",
        }
        mock_response.raise_for_status.return_value = None

        # Configure the post method
        mock.post.return_value = mock_response

        # Configure common request exceptions
        mock.exceptions = Mock()
        mock.exceptions.RequestException = Exception
        mock.exceptions.HTTPError = Exception
        mock.exceptions.ConnectionError = Exception
        mock.exceptions.Timeout = Exception

        yield mock
