from textfully import send


def test_send_success(mock_success_response):
    """Test successful message sending."""
    response = send("+16178856037", "Test message")
    assert response["id"] == "msg_123"
    assert response["status"] == "sent"


def test_send_with_emoji(mock_success_response):
    """Test sending message with emoji."""
    response = send("+16178856037", "Hello 👋 World 🌎!")
    assert response["id"] == "msg_123"


def test_send_with_template(mock_success_response):
    """Test sending message with template variables."""
    response = send("+16178856037", "Order #{{order_id}} has shipped!")
    assert response["id"] == "msg_123"
