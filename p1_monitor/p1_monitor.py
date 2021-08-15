"""Asynchronous Python client for the P1 Monitor API."""
from __future__ import annotations

import asyncio
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from aiohttp.client import ClientSession
import async_timeout
from yarl import URL

from .exceptions import P1MonitorConnectionError, P1MonitorError
from .models import SmartMeter, Settings, Phases


@dataclass
class P1Monitor:
    """Main class for handling connections with the P1 Monitor API."""

    def __init__(
        self,
        host: str,
        request_timeout: int = 10,
        session: ClientSession | None = None
    ) -> None:
        self._session = session
        self._close_session = False

        self.host = host
        self.request_timeout = request_timeout

    async def _request(
        self,
        uri: str,
        *,
        params: Mapping[str, str] | None = None,
    ) -> dict[str, Any]:
        """ """
        url = URL.build(
            scheme="http", host=self.host, path="/api/v1/"
        ).join(URL(uri))

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

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            raise P1MonitorError(
                "Unexpected response from the P1 Monitor device",
                {"Content-Type": content_type, "response": text},
            )

        return await response.json()

    async def smartmeter(self) -> SmartMeter:
        data = await self._request("smartmeter", params={"json": "object", "limit": 1})
        return SmartMeter.from_dict(data)

    async def settings(self) -> Settings:
        data = await self._request("configuration", params={"json": "object"})
        return Settings.from_dict(data)

    async def phases(self) -> Phases:
        data = await self._request("status", params={"json": "object"})
        return Phases.from_dict(data)

    async def close(self) -> None:
        """Close open client session."""
        if self._session and self._close_session:
            await self._session.close()

    async def __aenter__(self) -> P1Monitor:
        """Async enter.
        Returns:
            The P1M onitor object.
        """
        return self

    async def __aexit__(self, *_exc_info) -> None:
        """Async exit.
        Args:
            _exc_info: Exec type.
        """
        await self.close()