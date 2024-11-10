# Textfully Python SDK

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Build](https://github.com/gtfol/textfully-python/actions/workflows/python.yml/badge.svg)
[![codecov](https://codecov.io/gh/gtfol/textfully-python/branch/main/graph/badge.svg)](https://codecov.io/gh/gtfol/textfully-python)
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
textfully.send(
    "+16178856037", # verified phone number
    "Hello, world!"
)
```

Check out example implementations in the [examples](https://github.com/textfully/textfully-python/tree/main/examples) directory.

## Contributing

Contributing to the Python library is a great way to get involved with the Textfully community. Reach out to us on [Discord](https://discord.gg/Ct6FDCpFBU) or through email at [textfully@gtfol.inc](mailto:textfully@gtfol.inc) if you want to get involved.
