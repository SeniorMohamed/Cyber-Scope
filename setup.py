
from setuptools import setup, find_packages

setup(
    name="CyberScope",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "PyYAML",
        "flask",
    ],
)
