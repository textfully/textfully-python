import os
from dotenv import load_dotenv
import textfully

# Load environment variables from .env file
load_dotenv()

# Set your API key
textfully.api_key = os.getenv("TEXTFULLY_API_KEY")
to_number = (
    "your-verified-phone-number"  # Include international code (e.g. +1 for US/Canada)
)

# Send a simple message
response = textfully.send(to_number, "Hello, world!")
print(response)
