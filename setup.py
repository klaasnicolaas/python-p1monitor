#!/usr/bin/env python
"""The setup script"""
import os
import re
import sys

from setuptools import find_packages, setup


def read(*parts):
    """Read file."""
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)
    sys.stdout.write(filename)
    with open(filename, encoding="utf-8", mode="rt") as fp:
        return fp.read()


with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Klaas Schoute",
    author_email="hello@student-techlife.com",
    classifiers=[
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Asynchronous Python client for the P1 Monitor",
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.0.0",
    ],
    keywords=["p1", "monitor", "power", "energy", "api", "async", "client"],
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=readme,
    name="p1_monitor",
    packages=find_packages(include=["p1_monitor"]),
    url="https://github.com/klaasnicolaas/p1_monitor",
    version=os.environ.get("PACKAGE_VERSION"),
    zip_safe=False,
)