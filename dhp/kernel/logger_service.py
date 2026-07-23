"""
DHP Kernel - Logger Service
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Callable


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LoggerService:
    """
    Servicio de logging del Kernel.
    """

    def __init__(self) -> None:
        self._handlers: list[Callable] = [
            self._console_handler,
        ]

    def add_handler(self, handler: Callable) -> None:
        if handler not in self._handlers:
            self._handlers.append(handler)

    def remove_handler(self, handler: Callable) -> None:
        if handler in self._handlers:
            self._handlers.remove(handler)

    def log(
        self,
        level: LogLevel,
        message: str,
    ) -> None:
        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level.value,
            "message": message,
        }

        for handler in self._handlers:
            handler(record)

    def debug(self, message: str) -> None:
        self.log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        self.log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        self.log(LogLevel.WARNING, message)

    def error(self, message: str) -> None:
        self.log(LogLevel.ERROR, message)

    def critical(self, message: str) -> None:
        self.log(LogLevel.CRITICAL, message)

    @staticmethod
    def _console_handler(record: dict) -> None:
        print(
            f"[{record['timestamp']}] "
            f"[{record['level']}] "
            f"{record['message']}"
        )