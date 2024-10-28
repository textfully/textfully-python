"""
Textfully — iMessage & SMS API for Developers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An open-source Twilio alternative that lets developers send texts easily.

Basic usage:
    >>> import textfully
    >>> textfully.api_key = "your-api-key"
    >>> textfully.send("+16175555555", "Hello, world!")

Full documentation is available at https://textfully.dev/docs/python
"""

import requests
from typing import Optional, Dict, Any
from .version import __version__
from .exceptions import TextfullyError, AuthenticationError, APIError

api_key: Optional[str] = None
_base_url = "https://api.textfully.dev/v1"
_default_timeout = 30  # seconds


def _get_headers() -> Dict[str, str]:
    """Get the default headers for API requests."""
    if not api_key:
        raise AuthenticationError(
            "No API key provided. Set your API key using textfully.api_key = 'tx_apikey'"
        )

    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": f"textfully-python/{__version__}",
        "Accept": "application/json",
    }


def _handle_response(response: requests.Response) -> Dict[str, Any]:
    """Handle the API response and raise appropriate exceptions."""
    try:
        response_data = response.json()
    except ValueError:
        raise APIError(f"Invalid JSON response from API: {response.text}")

    if not 200 <= response.status_code < 300:
        error_message = response_data.get("error", {}).get("message", "Unknown error")
        error_type = response_data.get("error", {}).get("type", "api_error")

        if response.status_code == 401:
            raise AuthenticationError(f"Authentication failed: {error_message}")
        elif response.status_code == 400:
            raise APIError(f"Bad request: {error_message}")
        else:
            raise APIError(f"API request failed: {error_message} (Type: {error_type})")

    return response_data


def send(phone_number: str, text: str) -> Dict[str, Any]:
    """
    Send a text message using Textfully.

    Args:
        phone_number (str): The recipient's phone number in E.164 format (e.g., +16175555555)
        text (str): The message text to send, can include template variables like {{variable}}

    Returns:
        dict: The API response containing message details including:
            - id: The unique message ID
            - status: The message status ("queued", "sent", "delivered", "failed")
            - created_at: Timestamp when the message was created

    Raises:
        AuthenticationError: If no API key is set or authentication fails
        APIError: If the API request fails or returns an error
        ValueError: If the phone number format is invalid
    """
    # Enhanced phone number validation
    if not phone_number:
        raise ValueError(
            "Invalid phone number format. Must be in E.164 format (e.g., +16175555555)"
        )

    # Check for basic E.164 format requirements
    if not phone_number.startswith("+") or phone_number.count("+") > 1:
        raise ValueError(
            "Invalid phone number format. Must be in E.164 format (e.g., +16175555555)"
        )

    # Remove the plus for further validation
    digits = phone_number[1:]

    # Check if remaining characters are digits and length is valid (typically 10-15 digits)
    if (
        not digits.isdigit()
        or len(digits) < 10
        or len(digits) > 15
        or digits.startswith("0")
    ):
        raise ValueError(
            "Invalid phone number format. Must be in E.164 format (e.g., +16175555555)"
        )

    try:
        response = requests.post(
            f"{_base_url}/messages",
            json={"phone_number": phone_number, "text": text},
            headers=_get_headers(),
            timeout=_default_timeout,
        )

        return _handle_response(response)

    except requests.exceptions.Timeout:
        raise APIError("Request timed out. Please try again.")
    except requests.exceptions.RequestException as e:
        raise APIError(f"Request failed: {str(e)}")
