# pylint: disable=W0621
"""Asynchronous Python client for the P1 Monitor API."""

import asyncio

from p1monitor import P1Monitor, Phases, Settings, SmartMeter


async def main():
    """Test."""
    async with P1Monitor(
        host="example",
    ) as p1mon:
        smartmeter: SmartMeter = await p1mon.smartmeter()
        settings: Settings = await p1mon.settings()
        phases: Phases = await p1mon.phases()
        print(smartmeter)
        print()
        print("--- P1 Monitor | SmartMeter ---")
        print(f"Energy Consumption - High: {smartmeter.energy_consumption_high}")
        print(f"Energy Consumption - Low: {smartmeter.energy_consumption_low}")
        print(f"Energy Production - High: {smartmeter.energy_production_high}")
        print(f"Energy Production - Low: {smartmeter.energy_production_low}")
        print(f"Energy Tariff: {smartmeter.energy_tariff_period}")
        print()
        print(settings)
        print()
        print("--- P1 Monitor | Settings ---")
        print(
            f"Energy Consumption Price - High: {settings.energy_consumption_price_high}"
        )
        print(
            f"Energy Production Price - High: {settings.energy_production_price_high}"
        )
        print(f"Gas Price: {settings.gas_consumption_price}")
        print()
        print(phases)
        print()
        print("--- P1 Monitor | Phases ---")
        print(f"Current Phase L1: {phases.current_phase_l1}")
        print(f"Power Consumed Phase L1: {phases.power_consumed_phase_l1}")
        print(f"Power Produced Phase L1: {phases.power_produced_phase_l1}")
        print(f"Voltage Phase L1: {phases.voltage_phase_l1}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
