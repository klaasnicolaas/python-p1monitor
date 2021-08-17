"""Asynchronous Python client for the P1 Monitor API."""
from __future__ import annotations

import asyncio
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

import async_timeout
from aiohttp.client import ClientError, ClientResponseError, ClientSession
from yarl import URL

from .exceptions import P1MonitorConnectionError, P1MonitorError
from .models import Phases, Settings, SmartMeter


@dataclass
class P1Monitor:
    """Main class for handling connections with the P1 Monitor API."""

    def __init__(
        self, host: str, request_timeout: int = 10, session: ClientSession | None = None
    ) -> None:
        """Initialize connection with the P1 Monitor API.

        Args:
            host: Hostname or IP address of the P1 Monitor.
            request_timeout: An integer with the request timeout in seconds.
            session: Optional, shared, aiohttp client session.
        """
        self._session = session
        self._close_session = False

        self.host = host
        self.request_timeout = request_timeout

    async def request(
        self,
        uri: str,
        *,
        params: Mapping[str, str] | None = None,
    ) -> dict[str, Any]:
        """Handle a request to a P1 Monitor device.

        Args:
            uri: Request URI, without '/api/', for example, 'status'
            params: Extra options to improve or limit the response.

        Returns:
            A Python dictionary (JSON decoded) with the response from
            the P1 Monitor API.

        Raises:
            P1MonitorConnectionError: An error occurred while communicating
                with the P1 Monitor.
            P1MonitorError: Received an unexpected response from the P1 Monitor API.
        """
        url = URL.build(scheme="http", host=self.host, path="/api/").join(URL(uri))

        headers = {
            "Accept": "application/json, text/plain, */*",
        }

        if self._session is None:
            self._session = ClientSession()
            self._close_session = True

        try:
            with async_timeout.timeout(self.request_timeout):
                response = await self._session.request(
                    "GET",
                    url,
                    params=params,
                    headers=headers,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            raise P1MonitorConnectionError(
                "Timeout occurred while connecting to P1 Monitor device"
            ) from exception
        except (ClientError, ClientResponseError) as exception:
            raise P1MonitorConnectionError(
                "Error occurred while communicating with P1 Monitor device"
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            raise P1MonitorError(
                "Unexpected response from the P1 Monitor device",
                {"Content-Type": content_type, "response": text},
            )

        return await response.json()

    async def smartmeter(self) -> SmartMeter:
        """Get the latest values from you smart meter.

        Returns:
            A SmartMeter data object from the P1 Monitor API.
        """
        data = await self.request(
            "v1/smartmeter", params={"json": "object", "limit": 1}
        )
        return SmartMeter.from_dict(data)

    async def settings(self) -> Settings:
        """Receive the set price values for energy and gas.

        Returns:
            A Settings data object from the P1 Monitor API.
        """
        data = await self.request("v1/configuration", params={"json": "object"})
        return Settings.from_dict(data)

    async def phases(self) -> Phases:
        """Receive data from all phases on your smart meter.

        Returns:
            A Phases data object from the P1 Monitor API.
        """
        data = await self.request("v1/status", params={"json": "object"})
        return Phases.from_dict(data)

    async def close(self) -> None:
        """Close open client session."""
        if self._session and self._close_session:
            await self._session.close()

    async def __aenter__(self) -> P1Monitor:
        """Async enter.

        Returns:
            The P1 Monitor object.
        """
        return self

    async def __aexit__(self, *_exc_info) -> None:
        """Async exit.

        Args:
            _exc_info: Exec type.
        """
        await self.close()
