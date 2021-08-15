## Python - P1 Monitor API Client

<!-- PROJECT SHIELDS -->
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits]
[![GitHub Last Commit][last-commit-shield]][commits]
[![Contributors][contributors-shield]][contributors-url]

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

Asynchronous Python client for the P1 Monitor API.

## About

There are many ways to read the serial port (P1) of your smart meter and what you do with the data that comes out. With this python library your platform can read [P1 Monitor][p1-monitor] via the API and use the data for example for an integration in [Home Assistant][home-assistant].

## Installation

```bash
pip install p1_monitor
```

## Usage

```python
import asyncio

from p1_monitor import P1Monitor


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

### Phases
- Voltage phases L1/2/3
- Current Phases L1/2/3
- Power consumed phases L1/2/3
- Power Produced phases L1/2/3

### Settings
- Gas Consumption Tariff
- Energy Consumption Tariff Low/High
- Energy Production Tariff Low/High

## License

MIT License

Copyright (c) 2021 Klaas Schoute

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
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg?style=for-the-badge
[contributors-shield]: https://img.shields.io/github/contributors/klaasnicolaas/p1_monitor.svg?style=for-the-badge
[contributors-url]: https://github.com/klaasnicolaas/p1_monitor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/klaasnicolaas/p1_monitor.svg?style=for-the-badge
[forks-url]: https://github.com/klaasnicolaas/p1_monitor/network/members
[stars-shield]: https://img.shields.io/github/stars/klaasnicolaas/p1_monitor.svg?style=for-the-badge
[stars-url]: https://github.com/klaasnicolaas/p1_monitor/stargazers
[issues-shield]: https://img.shields.io/github/issues/klaasnicolaas/p1_monitor.svg?style=for-the-badge
[issues-url]: https://github.com/klaasnicolaas/p1_monitor/issues
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/p1_monitor.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/p1_monitor.svg?style=for-the-badge
[commits]: https://github.com/klaasnicolaas/p1_monitor/commits/master
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/p1_monitor.svg?style=for-the-badge

[p1-monitor]: https://www.ztatz.nl/p1-monitor
[home-assistant]: https://www.home-assistant.io
