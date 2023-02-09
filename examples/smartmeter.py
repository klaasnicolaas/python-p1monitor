# pylint: disable=W0621
"""Asynchronous Python client for the P1 Monitor API."""

import asyncio

from p1monitor import P1Monitor, SmartMeter


async def main() -> None:
    """Show example on getting P1 Monitor data."""
    async with P1Monitor(host="127.0.0.1") as client:
        smartmeter: SmartMeter = await client.smartmeter()

        print(smartmeter)
        print()
        print("--- P1 Monitor | SmartMeter ---")
        print(f"Power Consumption: {smartmeter.power_consumption}")
        print(f"Energy Consumption - High: {smartmeter.energy_consumption_high}")
        print(f"Energy Consumption - Low: {smartmeter.energy_consumption_low}")
        print()
        print(f"Power Production: {smartmeter.power_production}")
        print(f"Energy Production - High: {smartmeter.energy_production_high}")
        print(f"Energy Production - Low: {smartmeter.energy_production_low}")
        print(f"Energy Tariff: {smartmeter.energy_tariff_period}")
        print()
        print(f"Gas Consumption: {smartmeter.gas_consumption}")


if __name__ == "__main__":
    asyncio.run(main())
