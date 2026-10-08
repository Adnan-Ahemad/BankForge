"""Shared database access helpers for BankForge."""

from __future__ import annotations

from typing import Any, Dict


class BankForgeDatabase:
    """Minimal database client placeholder."""

    def __init__(self, connection_string: str | None = None):
        self.connection_string = connection_string

    def connect(self) -> Dict[str, Any]:
        return {"connection_string": self.connection_string, "status": "initialized"}

    def query(self, statement: str, params: tuple | list | None = None):
        _ = (statement, params)
        return []
