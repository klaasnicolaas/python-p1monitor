"""Models for P1 Monitor."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Status:
    """Return Status object from the P1 Monitor API response.
    Args:
        data: The data from the P1 Monitor API.
    Returns:
        A Status object.
    """

    python_version: str
    os_version: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Status:
        return Status(
            python_version=data[24]["STATUS"],
            os_version=data[21]["STATUS"],
        )

@dataclass
class SmartMeter:
    """Return SmartMeter object from the P1 Monitor API response.
    Args:
        data: The data from the P1 Monitor API.
    Returns:
        A SmartMeter object.
    """

    gas_consumption: float | None

    power_consumption: int | None
    energy_consumption_high: float | None
    energy_consumption_low: float | None

    power_production: int | None
    energy_production_high: float | None
    energy_production_low: float | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SmartMeter:
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
    """Return Settings object from the P1 Monitor API response.
    Args:
        data: The data from the P1 Monitor API.
    Returns:
        A Settings object.
    """
    version: str | None

    gas_consumption_tariff: float | None

    energy_consumption_tariff_high: float | None
    energy_consumption_tariff_low: float | None

    energy_production_tariff_high: float | None
    energy_production_tariff_low: float | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Settings:
        return Settings(
            version=data[0]["PARAMETER"],
            gas_consumption_tariff=data[15]["PARAMETER"],
            energy_consumption_tariff_low=data[1]["PARAMETER"],
            energy_consumption_tariff_high=data[2]["PARAMETER"],
            energy_production_tariff_low=data[3]["PARAMETER"],
            energy_production_tariff_high=data[4]["PARAMETER"],
        )