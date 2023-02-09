# pylint: disable=W0621
"""Asynchronous Python client for the P1 Monitor API."""

import asyncio

from p1monitor import P1Monitor, Settings


async def main() -> None:
    """Show example on getting P1 Monitor data."""
    async with P1Monitor(host="127.0.0.1") as client:
        settings: Settings = await client.settings()

        print(settings)
        energy_cons_high = settings.energy_consumption_price_high
        energy_cons_low = settings.energy_consumption_price_low
        energy_prod_high = settings.energy_production_price_high
        energy_prod_low = settings.energy_production_price_low
        print()
        print("--- P1 Monitor | Settings ---")
        print(f"Gas Price: {settings.gas_consumption_price}")
        print(f"Energy Consumption Price - High: {energy_cons_high}")
        print(f"Energy Consumption Price - Low: {energy_cons_low}")
        print(f"Energy Production Price - High: {energy_prod_high}")
        print(f"Energy Production Price - Low: {energy_prod_low}")


if __name__ == "__main__":
    asyncio.run(main())
