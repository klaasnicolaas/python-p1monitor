"""Basic tests for the P1Monitor device."""

# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from p1monitor import P1Monitor
from p1monitor.exceptions import P1MonitorConnectionError, P1MonitorError

from . import load_fixtures


async def test_json_request(
    aresponses: ResponsesMockServer,
    p1monitor_client: P1Monitor,
) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "192.168.1.2",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"status": "ok"}',
        ),
    )
    response = await p1monitor_client._request("test")
    assert response is not None
    await p1monitor_client.close()


async def test_different_port(aresponses: ResponsesMockServer) -> None:
    """Test different port is handled correctly."""
    aresponses.add(
        "192.168.1.2:84",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"status": "ok"}',
        ),
    )
    async with ClientSession() as session:
        p1monitor = P1Monitor("192.168.1.2", port=84, session=session)
        await p1monitor._request("test")
        await p1monitor.close()


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "192.168.1.2",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"status": "ok"}',
        ),
    )
    async with P1Monitor("192.168.1.2") as p1monitor:
        await p1monitor._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout from P1 Monitor."""

    # Faking a timeout by sleeping
    async def reponse_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
            text=load_fixtures("smartmeter.json"),
        )

    aresponses.add("192.168.1.2", "/api/test", "GET", reponse_handler)

    async with ClientSession() as session:
        client = P1Monitor(host="192.168.1.2", session=session, request_timeout=0.1)
        with pytest.raises(P1MonitorConnectionError):
            assert await client._request("test")


async def test_content_type(
    aresponses: ResponsesMockServer,
    p1monitor_client: P1Monitor,
) -> None:
    """Test request content type error from P1 Monitor."""
    aresponses.add(
        "192.168.1.2",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )
    with pytest.raises(P1MonitorError):
        assert await p1monitor_client._request("test")


async def test_client_error() -> None:
    """Test request client error from P1 Monitor."""
    async with ClientSession() as session:
        client = P1Monitor(host="192.168.1.2", session=session)
        with (
            patch.object(
                session,
                "request",
                side_effect=ClientError,
            ),
            pytest.raises(P1MonitorConnectionError),
        ):
            assert await client._request("test")
