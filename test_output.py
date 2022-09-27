# pylint: disable=W0621
"""Asynchronous Python client for the P1 Monitor API."""

import asyncio

from p1monitor import P1Monitor, Phases, Settings, SmartMeter, WaterMeter


async def main() -> None:
    """Test."""
    async with P1Monitor(
        host="127.0.0.1",
    ) as p1mon:
        smartmeter: SmartMeter = await p1mon.smartmeter()
        check_phases = False
        check_settings = False
        check_watermeter = True

        print(smartmeter)
        print()
        print("--- P1 Monitor | SmartMeter ---")
        print(f"Energy Consumption - High: {smartmeter.energy_consumption_high}")
        print(f"Energy Consumption - Low: {smartmeter.energy_consumption_low}")
        print(f"Energy Production - High: {smartmeter.energy_production_high}")
        print(f"Energy Production - Low: {smartmeter.energy_production_low}")
        print(f"Energy Tariff: {smartmeter.energy_tariff_period}")

        if check_settings:
            settings: Settings = await p1mon.settings()
            print()
            print(settings)
            energy_cons_high = settings.energy_consumption_price_high
            energy_prod_high = settings.energy_production_price_high
            print()
            print("--- P1 Monitor | Settings ---")
            print(f"Energy Consumption Price - High: {energy_cons_high}")
            print(f"Energy Production Price - High: {energy_prod_high}")
            print(f"Gas Price: {settings.gas_consumption_price}")

        if check_phases:
            phases: Phases = await p1mon.phases()
            print()
            print(phases)
            print()
            print("--- P1 Monitor | Phases ---")
            print(f"Current Phase L1: {phases.current_phase_l1}")
            print(f"Power Consumed Phase L1: {phases.power_consumed_phase_l1}")
            print(f"Power Produced Phase L1: {phases.power_produced_phase_l1}")
            print(f"Voltage Phase L1: {phases.voltage_phase_l1}")

        if check_watermeter:
            watermeter: WaterMeter = await p1mon.watermeter()
            print()
            print(watermeter)
            print()
            print("--- P1 Monitor | WaterMeter ---")
            print(f"Consumption Day: {watermeter.consumption_day}")
            print(f"Consumption Total: {watermeter.consumption_total}")
            print(f"Pulse Count: {watermeter.pulse_count}")


if __name__ == "__main__":
    asyncio.run(main())
