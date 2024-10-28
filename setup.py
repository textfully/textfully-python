from setuptools import setup, find_packages

setup(
    name="textfully",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Textfully",
    author_email="textfully@gtfol.inc",
    description="Textfully Python SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gtfol/textfully-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
