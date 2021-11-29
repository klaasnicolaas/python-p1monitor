"""Basic tests for the P1Monitor device."""
from unittest.mock import patch

import aiohttp
import pytest

from p1monitor import P1Monitor
from p1monitor.exceptions import P1MonitorConnectionError, P1MonitorError


@pytest.mark.asyncio
async def test_client_error():
    """Test request client error from P1 Monitor."""
    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        with patch.object(
            session, "request", side_effect=aiohttp.ClientError
        ), pytest.raises(P1MonitorConnectionError):
            assert await client.request("test")


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [401, 403])
async def test_http_error401(aresponses, status):
    """Test HTTP 401 response handling."""
    aresponses.add(
        "example.com",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(text="Give me energy!", status=status),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        with pytest.raises(P1MonitorConnectionError):
            assert await client.request("test")


@pytest.mark.asyncio
async def test_http_error400(aresponses):
    """Test HTTP 404 response handling."""
    aresponses.add(
        "example.com",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(text="Give me energy!", status=404),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        with pytest.raises(P1MonitorError):
            assert await client.request("test")


@pytest.mark.asyncio
async def test_http_error500(aresponses):
    """Test HTTP 500 response handling."""
    aresponses.add(
        "example.com",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(
            body=b'{"status":"nok"}',
            status=500,
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        with pytest.raises(P1MonitorError):
            assert await client.request("test")


@pytest.mark.asyncio
async def test_no_success(aresponses):
    """Test a message without a success message throws."""
    aresponses.add(
        "example.com",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(
            status=200,
            text='{"message": "no success"}',
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = P1Monitor(host="example.com", session=session)
        with pytest.raises(P1MonitorError):
            assert await client.request("test")
