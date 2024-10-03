"""Exceptions tests for the P1Monitor device."""

# pylint: disable=protected-access
import pytest
from aresponses import ResponsesMockServer

from p1monitor import P1Monitor
from p1monitor.exceptions import P1MonitorConnectionError, P1MonitorError


@pytest.mark.parametrize("status", [401, 403])
async def test_http_error401(
    aresponses: ResponsesMockServer,
    p1monitor_client: P1Monitor,
    status: int,
) -> None:
    """Test HTTP 401 response handling."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(text="Give me energy!", status=status),
    )
    with pytest.raises(P1MonitorConnectionError):
        assert await p1monitor_client._request("test")


async def test_http_error404(
    aresponses: ResponsesMockServer,
    p1monitor_client: P1Monitor,
) -> None:
    """Test HTTP 404 response handling."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(text="Give me energy!", status=404),
    )
    with pytest.raises(P1MonitorError):
        assert await p1monitor_client._request("test")


async def test_http_error500(
    aresponses: ResponsesMockServer,
    p1monitor_client: P1Monitor,
) -> None:
    """Test HTTP 500 response handling."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(
            body=b'{"status":"nok"}',
            status=500,
        ),
    )
    with pytest.raises(P1MonitorError):
        assert await p1monitor_client._request("test")


async def test_no_success(
    aresponses: ResponsesMockServer,
    p1monitor_client: P1Monitor,
) -> None:
    """Test a message without a success message throws."""
    aresponses.add(
        "192.168.1.2",
        "/api/v1/smartmeter",
        "GET",
        aresponses.Response(
            status=200,
            text='{"message": "no success"}',
        ),
    )
    with pytest.raises(P1MonitorError):
        assert await p1monitor_client._request("test")
