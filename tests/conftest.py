"""Fixture for the P1Monitor tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from p1monitor import P1Monitor


@pytest.fixture(name="p1monitor_client")
async def client() -> AsyncGenerator[P1Monitor, None]:
    """Return a P1Monitor client."""
    async with (
        ClientSession() as session,
        P1Monitor(host="192.168.1.2", session=session) as p1monitor_client,
    ):
        yield p1monitor_client
