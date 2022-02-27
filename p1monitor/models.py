"""Models for P1 Monitor."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class EnergyTariff(str, Enum):
    """Enumeration representing the rate period."""

    LOW = "low"
    HIGH = "high"


@dataclass
class SmartMeter:
    """Object representing an SmartMeter response from P1 Monitor."""

    gas_consumption: float | None
    energy_tariff_period: str | None

    power_consumption: int | None
    energy_consumption_high: float | None
    energy_consumption_low: float | None

    power_production: int | None
    energy_production_high: float | None
    energy_production_low: float | None

    @staticmethod
    def from_dict(data: dict[str | int, Any]) -> SmartMeter:
        """Return SmartMeter object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A SmartMeter object.
        """

        def energy_tariff(tariff: str) -> EnergyTariff:
            """Return API energy_tariff information.

            Args:
                tariff: The provided tariff code from the API.

            Returns:
                The energy tariff period class.
            """
            if tariff == "P":
                return EnergyTariff.HIGH
            return EnergyTariff.LOW

        data = data[0]
        return SmartMeter(
            gas_consumption=data.get("CONSUMPTION_GAS_M3"),
            power_consumption=data.get("CONSUMPTION_W"),
            energy_consumption_high=data.get("CONSUMPTION_KWH_HIGH"),
            energy_consumption_low=data.get("CONSUMPTION_KWH_LOW"),
            power_production=data.get("PRODUCTION_W"),
            energy_production_high=data.get("PRODUCTION_KWH_HIGH"),
            energy_production_low=data.get("PRODUCTION_KWH_LOW"),
            energy_tariff_period=energy_tariff(str(data.get("TARIFCODE"))),
        )


@dataclass
class Settings:
    """Object representing an Settings response from P1 Monitor."""

    gas_consumption_price: float | None

    energy_consumption_price_high: float | None
    energy_consumption_price_low: float | None

    energy_production_price_high: float | None
    energy_production_price_low: float | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Settings:
        """Return Settings object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A Settings object.
        """

        return Settings(
            gas_consumption_price=search(15, data, "configuration"),
            energy_consumption_price_low=search(1, data, "configuration"),
            energy_consumption_price_high=search(2, data, "configuration"),
            energy_production_price_low=search(3, data, "configuration"),
            energy_production_price_high=search(4, data, "configuration"),
        )


@dataclass
class Phases:
    """Object representing an Phases response from P1 Monitor."""

    voltage_phase_l1: float | None
    voltage_phase_l2: float | None
    voltage_phase_l3: float | None

    current_phase_l1: float | None
    current_phase_l2: float | None
    current_phase_l3: float | None

    power_consumed_phase_l1: int | None
    power_consumed_phase_l2: int | None
    power_consumed_phase_l3: int | None

    power_produced_phase_l1: int | None
    power_produced_phase_l2: int | None
    power_produced_phase_l3: int | None

    @staticmethod
    def from_dict(data: dict[str | int, Any]) -> Phases:
        """Return Phases object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A Phases object.
        """

        def convert(value: int) -> int | None:
            """Convert values from kW to W.

            Args:
                value: The current value.

            Returns:
                Value in Watt (W).
            """
            if value is not None:
                value = int(float(value) * 1000)
                return value
            return None

        return Phases(
            voltage_phase_l1=search(103, data, "status"),
            voltage_phase_l2=search(104, data, "status"),
            voltage_phase_l3=search(105, data, "status"),
            current_phase_l1=search(100, data, "status"),
            current_phase_l2=search(101, data, "status"),
            current_phase_l3=search(102, data, "status"),
            power_consumed_phase_l1=convert(search(74, data, "status")),
            power_consumed_phase_l2=convert(search(75, data, "status")),
            power_consumed_phase_l3=convert(search(76, data, "status")),
            power_produced_phase_l1=convert(search(77, data, "status")),
            power_produced_phase_l2=convert(search(78, data, "status")),
            power_produced_phase_l3=convert(search(79, data, "status")),
        )


@dataclass
class WaterMeter:
    """Object representing an WaterMeter response from P1 Monitor."""

    consumption_day: int | None
    consumption_total: float | None
    pulse_count: int | None

    @staticmethod
    def from_dict(data: dict[str | int, Any]) -> WaterMeter:
        """Return WaterMeter object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A WaterMeter object.
        """

        data = data[0]
        return WaterMeter(
            consumption_day=data.get("WATERMETER_CONSUMPTION_LITER"),
            consumption_total=data.get("WATERMETER_CONSUMPTION_TOTAL_M3"),
            pulse_count=data.get("WATERMETER_PULS_COUNT"),
        )


def search(position: int, data: Any, service: str) -> Any:
    """Find the correct value in the json data file.

    Args:
        position: The position ID number.
        data: The JSON list which is requested from the API.
        service: Type of dataclass.

    Returns:
        The value that corresponds to the specified position.
    """
    for i in data:
        if service == "configuration" and i["CONFIGURATION_ID"] == position:
            return i["PARAMETER"]
        if service == "status" and i["STATUS_ID"] == position:
            return i["STATUS"]
    return None
