# pylint: disable=W0621
"""Asynchronous Python client for the P1 Monitor API."""

import asyncio

from p1monitor import P1Monitor, WaterMeter


async def main() -> None:
    """Show example on getting P1 Monitor data."""
    async with P1Monitor(host="127.0.0.1") as client:
        watermeter: WaterMeter = await client.watermeter()

        print(watermeter)
        print()
        print("--- P1 Monitor | WaterMeter ---")
        print(f"Consumption Day: {watermeter.consumption_day}")
        print(f"Consumption Total: {watermeter.consumption_total}")
        print(f"Pulse Count: {watermeter.pulse_count}")


if __name__ == "__main__":
    asyncio.run(main())
