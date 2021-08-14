"""Exceptions for P1 Monitor."""


class P1MonitorError(Exception):
    """Generic P1 Monitor exception."""


class P1MonitorConnectionError(P1MonitorError):
    """P1 Monitor connection exception."""