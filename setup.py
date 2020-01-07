from setuptools import setup, find_packages

setup(
    name="ddconfig",
    description="Configuration using command line, config file and environment variables using a dataclass",
    version="0.0.1",
    author="Nick Spain",
    url="https://github.com/nick96/ddconfig",
    packages=find_packages(exclude=["tests"]),
    keywords=["config", "data-class"],
)