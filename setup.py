from setuptools import setup, find_packages

setup(
    name="textfully",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Textfully",
    author_email="support@textfully.dev",
    description="Official Python SDK for Textfully - iMessage & SMS API for Developers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://textfully.dev",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
