# Textfully Python SDK

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/textfully)](https://pypi.org/project/textfully)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textfully)](https://pypi.org/project/textfully)

---

The official Python SDK for [Textfully](https://textfully.dev) — The Open Source Twilio Alternative.

## Installation

```bash
pip install textfully
```

## Setup

First, you need to generate an API key from the [Textfully Dashboard](https://textfully.dev/dashboard/api/keys).

## Quick Start

```python
import textfully

# Set your API key
textfully.api_key = "tx_apikey"

# Send a message
response = textfully.send(
    "+16175555555", # your verified phone number
    "Hello, world!"
)
```
