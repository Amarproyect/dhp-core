"""
DHP Kernel - Event Bus

Bus de eventos interno.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable

from .event import Event


EventHandler = Callable[[Event], None]


class EventBus:
    """
    Bus de eventos síncrono del Kernel.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Registra un manejador para un evento.
        """
        self._subscribers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Elimina un manejador.
        """
        if handler in self._subscribers[event_name]:
            self._subscribers[event_name].remove(handler)

    def publish(self, event: Event) -> None:
        """
        Publica un evento.
        """
        for handler in self._subscribers.get(event.name, []):
            handler(event)

    def clear(self) -> None:
        """
        Elimina todas las suscripciones.
        """
        self._subscribers.clear()