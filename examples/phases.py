# pylint: disable=W0621
"""Asynchronous Python client for the P1 Monitor API."""

import asyncio

from p1monitor import P1Monitor, Phases


async def main() -> None:
    """Show example on getting P1 Monitor data."""
    async with P1Monitor(host="127.0.0.1") as client:
        phases: Phases = await client.phases()

        print(phases)
        print()
        print("--- P1 Monitor | Phases ---")
        print(f"Voltage Phase L1: {phases.voltage_phase_l1}")
        print(f"Voltage Phase L2: {phases.voltage_phase_l2}")
        print(f"Voltage Phase L3: {phases.voltage_phase_l3}")
        print()
        print(f"Current Phase L1: {phases.current_phase_l1}")
        print(f"Current Phase L2: {phases.current_phase_l2}")
        print(f"Current Phase L3: {phases.current_phase_l3}")
        print()
        print(f"Power Consumed Phase L1: {phases.power_consumed_phase_l1}")
        print(f"Power Consumed Phase L2: {phases.power_consumed_phase_l2}")
        print(f"Power Consumed Phase L3: {phases.power_consumed_phase_l3}")
        print()
        print(f"Power Produced Phase L1: {phases.power_produced_phase_l1}")
        print(f"Power Produced Phase L2: {phases.power_produced_phase_l2}")
        print(f"Power Produced Phase L3: {phases.power_produced_phase_l3}")


if __name__ == "__main__":
    asyncio.run(main())
