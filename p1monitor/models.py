"""Models for P1 Monitor."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SmartMeter:
    """Object representing an SmartMeter response from P1 Monitor."""

    gas_consumption: float | None

    power_consumption: int | None
    energy_consumption_high: float | None
    energy_consumption_low: float | None

    power_production: int | None
    energy_production_high: float | None
    energy_production_low: float | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SmartMeter:
        """Return SmartMeter object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A SmartMeter object.
        """
        data = data[0]
        return SmartMeter(
            gas_consumption=data.get("CONSUMPTION_GAS_M3"),
            power_consumption=data.get("CONSUMPTION_W"),
            energy_consumption_high=data.get("CONSUMPTION_KWH_HIGH"),
            energy_consumption_low=data.get("CONSUMPTION_KWH_LOW"),
            power_production=data.get("PRODUCTION_W"),
            energy_production_high=data.get("PRODUCTION_KWH_HIGH"),
            energy_production_low=data.get("PRODUCTION_KWH_LOW"),
        )


@dataclass
class Settings:
    """Object representing an Settings response from P1 Monitor."""

    gas_consumption_tariff: float | None

    energy_consumption_high_tariff: float | None
    energy_consumption_low_tariff: float | None

    energy_production_high_tariff: float | None
    energy_production_low_tariff: float | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Settings:
        """Return Settings object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A Settings object.
        """

        return Settings(
            gas_consumption_tariff=search(15, data, "configuration"),
            energy_consumption_low_tariff=search(1, data, "configuration"),
            energy_consumption_high_tariff=search(2, data, "configuration"),
            energy_production_low_tariff=search(3, data, "configuration"),
            energy_production_high_tariff=search(4, data, "configuration"),
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
    def from_dict(data: dict[str, Any]) -> Phases:
        """Return Phases object from the P1 Monitor API response.

        Args:
            data: The data from the P1 Monitor API.

        Returns:
            A Phases object.
        """

        def convert(value):
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


def search(position, data, service):
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
