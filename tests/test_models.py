"""Test the models."""

import pytest
from aiohttp import ClientSession
from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from p1monitor import (
    P1Monitor,
    P1MonitorConnectionError,
    P1MonitorNoDataError,
    Phases,
    Settings,
    SmartMeter,
    WaterMeter,
)

from . import load_fixtures


async def test_smartmeter(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    p1monitor_client: P1Monitor,
) -> None:
    """Test request from a P1 Monitor device - SmartMeter object."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(
            text=load_fixtures("smartmeter.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )
    smartmeter: SmartMeter = await p1monitor_client.smartmeter()
    assert smartmeter == snapshot


async def test_phases(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    p1monitor_client: P1Monitor,
) -> None:
    """Test request from a P1 Monitor device - Phases object."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/status",
        "GET",
        aresponses.Response(
            text=load_fixtures("phases.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )
    phases: Phases = await p1monitor_client.phases()
    assert phases == snapshot


async def test_watermeter(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    p1monitor_client: P1Monitor,
) -> None:
    """Test request from a P1 Monitor device - WaterMeter object."""
    aresponses.add(
        "192.168.1.2",
        "/api/v2/watermeter/day",
        "GET",
        aresponses.Response(
            text=load_fixtures("watermeter.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )
    watermeter: WaterMeter = await p1monitor_client.watermeter()
    assert watermeter == snapshot


async def test_no_watermeter_data_new(aresponses: ResponsesMockServer) -> None:
    """Test no WaterMeter data from P1 Monitor device."""
    aresponses.add(
        "192.168.1.2",
        "/api/v2/watermeter/day",
        "GET",
        aresponses.Response(
            text=load_fixtures("no_data.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )

    async with ClientSession() as session:
        client = P1Monitor(host="192.168.1.2", session=session)
        with pytest.raises(P1MonitorNoDataError):
            await client.watermeter()


async def test_no_watermeter_data_old(aresponses: ResponsesMockServer) -> None:
    """Test no WaterMeter data from P1 Monitor device."""
    aresponses.add(
        "192.168.1.2",
        "/api/v2/watermeter/day",
        "GET",
        aresponses.Response(
            status=404,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )

    async with ClientSession() as session:
        client = P1Monitor(host="192.168.1.2", session=session)
        with pytest.raises(P1MonitorConnectionError):
            await client.watermeter()


async def test_settings(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    p1monitor_client: P1Monitor,
) -> None:
    """Test request from a P1 Monitor device - Settings object."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/configuration",
        "GET",
        aresponses.Response(
            text=load_fixtures("settings.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
    )
    settings: Settings = await p1monitor_client.settings()
    assert settings == snapshot
