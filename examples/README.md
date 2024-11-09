# Textfully Examples

This directory contains example implementations of the Textfully Python SDK.

## Prerequisites

1. Generate an API key from the [Textfully Dashboard](https://textfully.dev/dashboard/api/keys)

2. Create a `.env` file in the examples directory by copying `.env.example`:

```sh
cp .env.example .env
```

3. Update the `.env` file with your API key from step 1:

```sh
TEXTFULLY_API_KEY=your-textfully-api-key
```

4. Update the `to_number` variable in `send_text.py` with your verified phone number:

```python
to_number = "your-verified-phone-number"  # Include international code (e.g. +1 for US/Canada)
```

### Running the Example

```sh
python send_text.py
```
