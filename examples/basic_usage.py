import os
import textfully

# Set your API key
textfully.api_key = os.getenv("TEXTFULLY_API_KEY", "your_api_key_here")

# Send a simple message
response = textfully.send(
    "+16175555555",  # your verified phone number
    "Hello, world!",
)
print(f"Message sent! ID: {response['id']}")

# Send a message with variables
company_name = "Acme"
order_id = "12345"

response = textfully.send(
    "+16175555555",
    "Thanks for ordering! Your {{company_name}} order #{{order_id}} ships tomorrow.",
)
print(f"Message sent! ID: {response['id']}")
