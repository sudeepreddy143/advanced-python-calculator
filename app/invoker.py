"""
Manages execution of commands in the calculator.
"""
import logging
from typing import Dict, Type
from app.commands.base import BaseCommand

logger = logging.getLogger("app")


class CommandInvoker:
    """Invoker for managing and executing commands in the REPL."""

    def __init__(self):
        """Initialize an empty command registry."""
        self._commands: Dict[str, Type[BaseCommand]] = {}

    def register_command(self, name: str, command: Type[BaseCommand]):
        """Register a new command."""
        self._commands[name] = command

    def execute_command(self, name: str, *args):
        """Execute a registered command synchronously."""
        if name not in self._commands:
            logger.warning("Unknown command: %s", name)
            print("Unknown command. Type 'menu' to see available commands.")
            return None

        result = self._commands[name].execute(*args)
        print(f"Result: {result}")

        logger.info("Executed: %s(%s) -> %s", name, ", ".join(map(str, args)), result)
        return result

    def get_available_commands(self):
        """Return a dictionary of registered command names and their instances."""
        return self._commands  # ✅ Fix: Return actual command objects
