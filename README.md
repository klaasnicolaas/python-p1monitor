## Python - P1 Monitor API Client

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]

[![Code Quality][code-quality-shield]][code-quality]
[![Maintainability][maintainability-shield]][maintainability-url]
[![Code Coverage][codecov-shield]][codecov-url]

[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]

Asynchronous Python client for the P1 Monitor API.

## About

There are many ways to read the serial port (P1) of your smart meter and what you do with the data that comes out. With this python library your platform can read [P1 Monitor][p1-monitor] via the API and use the data for example for an integration in [Home Assistant][home-assistant].

## Installation

```bash
pip install p1monitor
```

## Usage

```python
import asyncio

from p1monitor import P1Monitor


async def main():
    """Show example on getting P1 Monitor data."""
    async with P1Monitor(host="example_host") as client:
        smartmeter = await client.smartmeter()
        print(smartmeter)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Data

There is a lot of data that you can read via the API:

### SmartMeter
- Gas Consumption
- Power Consumption / Production
- Energy Consumption Low/High
- Energy Production Low/High
- Energy Tariff Period

### Phases
- Voltage phases L1/2/3
- Current Phases L1/2/3
- Power consumed phases L1/2/3
- Power Produced phases L1/2/3

### WaterMeter
- Day Consumption (liters)
- Total Consumption (m3)
- Day Pulse count

### Settings
- Gas Consumption Price
- Energy Consumption Price Low/High
- Energy Production Price Low/High

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager.

You need at least:

- Python 3.9+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Setup the pre-commit check, you must run this inside the virtual environment:

```bash
pre-commit install
```

*Now you're all set to get started!*

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## License

MIT License

Copyright (c) 2021-2022 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-p1monitor/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-p1monitor/actions/workflows/tests.yaml
[code-quality-shield]: https://img.shields.io/lgtm/grade/python/g/klaasnicolaas/python-p1monitor.svg?logo=lgtm&logoWidth=18
[code-quality]: https://lgtm.com/projects/g/klaasnicolaas/python-p1monitor/context:python
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-p1monitor.svg
[commits-url]: https://github.com/klaasnicolaas/python-p1monitor/commits/main
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-p1monitor/branch/main/graph/badge.svg?token=G4FIVHJVZR
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-p1monitor
[forks-shield]: https://img.shields.io/github/forks/klaasnicolaas/python-p1monitor.svg
[forks-url]: https://github.com/klaasnicolaas/python-p1monitor/network/members
[issues-shield]: https://img.shields.io/github/issues/klaasnicolaas/python-p1monitor.svg
[issues-url]: https://github.com/klaasnicolaas/python-p1monitor/issues
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-p1monitor.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-p1monitor.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2022.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/443c476612a574d82467/maintainability
[maintainability-url]: https://codeclimate.com/github/klaasnicolaas/python-p1monitor/maintainability
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[pypi]: https://pypi.org/project/p1monitor/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/p1monitor
[typing-shield]: https://github.com/klaasnicolaas/python-p1monitor/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-p1monitor/actions/workflows/typing.yaml
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-p1monitor.svg
[releases]: https://github.com/klaasnicolaas/python-p1monitor/releases
[stars-shield]: https://img.shields.io/github/stars/klaasnicolaas/python-p1monitor.svg
[stars-url]: https://github.com/klaasnicolaas/python-p1monitor/stargazers

[p1-monitor]: https://www.ztatz.nl/p1-monitor
[home-assistant]: https://www.home-assistant.io
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
