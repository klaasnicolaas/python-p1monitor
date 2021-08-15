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
            gas_consumption_tariff=data[15]["PARAMETER"],
            energy_consumption_low_tariff=data[1]["PARAMETER"],
            energy_consumption_high_tariff=data[2]["PARAMETER"],
            energy_production_low_tariff=data[3]["PARAMETER"],
            energy_production_high_tariff=data[4]["PARAMETER"],
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
        return Phases(
            voltage_phase_l1=data[102]["STATUS"],
            voltage_phase_l2=data[103]["STATUS"],
            voltage_phase_l3=data[104]["STATUS"],
            current_phase_l1=data[99]["STATUS"],
            current_phase_l2=data[100]["STATUS"],
            current_phase_l3=data[101]["STATUS"],
            power_consumed_phase_l1=convert(data[73]["STATUS"]),
            power_consumed_phase_l2=convert(data[74]["STATUS"]),
            power_consumed_phase_l3=convert(data[75]["STATUS"]),
            power_produced_phase_l1=convert(data[76]["STATUS"]),
            power_produced_phase_l2=convert(data[77]["STATUS"]),
            power_produced_phase_l3=convert(data[78]["STATUS"]),
        )


def convert(data):
    """Convert values from kW to W.

    Args:
        data: The value.

    Returns:
        Value in Watt (W).
    """
    value = int(float(data) * 1000)
    return value
