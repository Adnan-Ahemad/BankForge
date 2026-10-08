"""FastMCP integration placeholder for BankForge."""

from __future__ import annotations


class FastMCP:
    """Placeholder class for an MCP-compatible server adapter."""

    def __init__(self, name: str = "bankforge"):
        self.name = name

    def tool(self, func):
        return func
