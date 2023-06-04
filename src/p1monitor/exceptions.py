"""Exceptions for P1 Monitor."""


class P1MonitorError(Exception):
    """Generic P1 Monitor exception."""


class P1MonitorConnectionError(P1MonitorError):
    """P1 Monitor connection exception."""


class P1MonitorNoDataError(P1MonitorError):
    """P1 Monitor no data exception."""
