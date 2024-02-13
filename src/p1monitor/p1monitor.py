"""Asynchronous Python client for the P1 Monitor API."""
from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Self, cast

from aiohttp import ClientError, ClientSession
from aiohttp.hdrs import METH_GET
from yarl import URL

from .exceptions import P1MonitorConnectionError, P1MonitorError, P1MonitorNoDataError
from .models import Phases, Settings, SmartMeter, WaterMeter


@dataclass
class P1Monitor:
    """Main class for handling connections with the P1 Monitor API."""

    host: str
    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to a P1 Monitor device.

        Args:
        ----
            uri: Request URI, without '/api/', for example, 'status'
            method: HTTP Method to use.
            params: Extra options to improve or limit the response.

        Returns:
        -------
            A Python dictionary (JSON decoded) with the response from
            the P1 Monitor API.

        Raises:
        ------
            P1MonitorConnectionError: An error occurred while communicating
                with the P1 Monitor.
            P1MonitorError: Received an unexpected response from the P1 Monitor API.

        """
        version = metadata.version(__package__)
        url = URL.build(scheme="http", host=self.host, path="/api/").join(URL(uri))

        headers = {
            "User-Agent": f"PythonP1Monitor/{version}",
            "Accept": "application/json, text/plain, */*",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with asyncio.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                )
                response.raise_for_status()

        except TimeoutError as exception:
            msg = "Timeout occurred while connecting to P1 Monitor device"
            raise P1MonitorConnectionError(
                msg,
            ) from exception
        except (ClientError, socket.gaierror) as exception:
            if "watermeter" in uri and response.status == 404:
                msg = "No water meter is connected to P1 Monitor device"
                raise P1MonitorConnectionError(msg) from exception
            msg = "Error occurred while communicating with P1 Monitor device"
            raise P1MonitorConnectionError(msg) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            msg = "Unexpected response from the P1 Monitor device"
            raise P1MonitorError(
                msg,
                {"Content-Type": content_type, "response": text},
            )

        return cast(dict[str, Any], await response.json())

    async def smartmeter(self) -> SmartMeter:
        """Get the latest values from you smart meter.

        Returns
        -------
            A SmartMeter data object from the P1 Monitor API.

        """
        data = await self._request(
            "v1/smartmeter",
            params={"json": "object", "limit": 1},
        )
        return SmartMeter.from_dict(data)

    async def settings(self) -> Settings:
        """Receive the set price values for energy and gas.

        Returns
        -------
            A Settings data object from the P1 Monitor API.

        """
        data = await self._request("v1/configuration", params={"json": "object"})
        return Settings.from_dict(data)

    async def phases(self) -> Phases:
        """Receive data from all phases on your smart meter.

        Returns
        -------
            A Phases data object from the P1 Monitor API.

        """
        data = await self._request("v1/status", params={"json": "object"})
        return Phases.from_dict(data)

    async def watermeter(self) -> WaterMeter:
        """Get the latest values from you water meter.

        Returns
        -------
            A WaterMeter data object from the P1 Monitor API.

        Raises
        ------
            P1MonitorNoDataError: No data was received from the P1 Monitor API.

        """
        data = await self._request(
            "v2/watermeter/day",
            params={"json": "object", "limit": 1},
        )
        if data == []:
            msg = "No data received from P1 Monitor"
            raise P1MonitorNoDataError(msg)
        return WaterMeter.from_dict(data)

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The P1 Monitor object.

        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.

        """
        await self.close()
