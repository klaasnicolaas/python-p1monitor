## Python P1 Monitor API Client

Asynchronous Python client for the P1 Monitor API.

## About

There are many ways to read the serial port (P1) of your smart meter and what you do with the data that comes out. With this pyhton library your platform can read [P1 Monitor][p1-monitor] via the API and use the data for example for an integration in [Home Assistant][home-assistant].

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

[p1-monitor]: https://www.ztatz.nl/p1-monitor
[home-assistant]: https://www.home-assistant.io