"""
DHP Kernel - Event Bus

Bus de eventos interno del Kernel.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any


EventHandler = Callable[[Any], None]


class EventBus:
    """
    Bus de eventos simple.

    Permite publicar eventos y registrar escuchadores.
    """

    def __init__(self) -> None:

        self._listeners: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event: str,
        handler: EventHandler,
    ) -> None:

        self._listeners[event].append(handler)

    def publish(
        self,
        event: str,
        payload: Any = None,
    ) -> None:

        for handler in self._listeners.get(event, []):

            handler(payload)