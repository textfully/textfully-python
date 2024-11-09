# Deployment Guide

## Prerequisites

- PyPI account with login credentials
- Write access to the PyPI package
- Python 3.7+ installed
- pip and build tools: `pip install --upgrade pip build twine`

## Publishing Steps

1. Update and test:

```sh
git pull origin main
pip install -r requirements.txt
pytest
```

2. Update version number in [setup.py](setup.py) and [version.py](textfully/version.py) and commit:

```sh
git add setup.py textfully/version.py
git commit -m "Version vX.Y.Z"
git tag vX.Y.Z
```

3. Push to GitHub:

```sh
git push && git push --tags
```

GitHub Actions will automatically run tests and publish to PyPI.
