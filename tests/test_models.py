"""Test the models."""
import aiohttp
import pytest

from p1monitor import P1Monitor, Phases, Settings, SmartMeter

from . import load_fixtures


@pytest.mark.asyncio
async def test_smartmeter(aresponses):
    """Test request from a P1 Monitor device - SmartMeter object."""
    aresponses.add(
        "example.com",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(
            text=load_fixtures("smartmeter.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        smartmeter: SmartMeter = await client.smartmeter()
        assert smartmeter
        assert smartmeter.gas_consumption == 2289.967
        assert smartmeter.power_consumption == 935
        assert smartmeter.power_production == 0
        assert smartmeter.energy_consumption_high == 2996.141
        assert smartmeter.energy_consumption_low == 5436.256
        assert smartmeter.energy_production_high == 4408.947
        assert smartmeter.energy_production_low == 1575.502
        assert smartmeter.energy_tariff_period == "low"


@pytest.mark.asyncio
async def test_phases(aresponses):
    """Test request from a P1 Monitor device - Phases object."""
    aresponses.add(
        "example.com",
        "/api/v1/status",
        "GET",
        aresponses.Response(
            text=load_fixtures("phases.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        phases: Phases = await client.phases()
        assert phases
        assert phases.current_phase_l1 == "4.0"
        assert phases.power_consumed_phase_l1 == 863
        assert phases.power_produced_phase_l1 == 0
        assert phases.voltage_phase_l1 == "229.0"


@pytest.mark.asyncio
async def test_settings(aresponses):
    """Test request from a P1 Monitor device - Settings object."""
    aresponses.add(
        "example.com",
        "/api/v1/configuration",
        "GET",
        aresponses.Response(
            text=load_fixtures("settings.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        settings: Settings = await client.settings()
        assert settings
        assert settings.energy_consumption_price_high == "0.24388"
        assert settings.energy_consumption_price_low == "0.22311"
        assert settings.energy_production_price_high == "0.24388"
        assert settings.energy_production_price_low == "0.22311"