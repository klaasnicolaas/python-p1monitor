<!-- Banner -->
![alt Banner of the P1 Monitor package](https://raw.githubusercontent.com/klaasnicolaas/python-p1monitor/main/assets/header_p1monitor-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]
[![Code Coverage][codecov-shield]][codecov-url]

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
    async with P1Monitor(host="192.168.1.2", port=80) as client:
        smartmeter = await client.smartmeter()
        watermeter = await client.watermeter()
        settings = await client.settings()
        phases = await client.phases()
        print(smartmeter)
        print(watermeter)
        print(settings)
        print(phases)


if __name__ == "__main__":
    asyncio.run(main())
```

More examples can be found in the [examples folder](./examples/).

## Class: `P1Monitor`

This is the main class that you will use to interact with the P1 Monitor.

| Parameter | Required | Description                                  |
| --------- | -------- | -------------------------------------------- |
| `host`    | `True`   | The IP address of the P1 Monitor.            |
| `port`    | `False`  | The port of the P1 Monitor. Default is `80`. |

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

> [!IMPORTANT]
> WaterMeter is only available when you run version 1.1.0 or higher due the use of the new v2 API url.

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

The simplest way to begin is by utilizing the [Dev Container][devcontainer]
feature of Visual Studio Code or by opening a CodeSpace directly on GitHub.
By clicking the button below you immediately start a Dev Container in Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.12+
- [Poetry][poetry-install]

### Installation

Install all packages, including all development requirements:

```bash
poetry install
```

_Poetry creates by default an virtual environment where it installs all
necessary pip packages_.

### Pre-commit

This repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. To setup the pre-commit check, run:

```bash
poetry run pre-commit install
```

And to run all checks and tests manually, use the following command:

```bash
poetry run pre-commit run --all-files
```

### Testing

It uses [pytest](https://docs.pytest.org/en/stable/) as the test framework. To run the tests:

```bash
poetry run pytest
```

To update the [syrupy](https://github.com/tophat/syrupy) snapshot tests:

```bash
poetry run pytest --snapshot-update
```

## License

MIT License

Copyright (c) 2021-2025 Klaas Schoute

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
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-p1monitor.svg
[commits-url]: https://github.com/klaasnicolaas/python-p1monitor/commits/main
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-p1monitor/branch/main/graph/badge.svg?token=G4FIVHJVZR
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-p1monitor
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/klaasnicolaas/python-p1monitor
[downloads-shield]: https://img.shields.io/pypi/dm/p1monitor
[downloads-url]: https://pypistats.org/packages/p1monitor
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-p1monitor.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-p1monitor.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[pypi]: https://pypi.org/project/p1monitor/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/p1monitor
[typing-shield]: https://github.com/klaasnicolaas/python-p1monitor/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-p1monitor/actions/workflows/typing.yaml
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-p1monitor.svg
[releases]: https://github.com/klaasnicolaas/python-p1monitor/releases

[p1-monitor]: https://www.ztatz.nl/p1-monitor
[home-assistant]: https://www.home-assistant.io
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
