import multiprocessing
from typing import Dict, Type
from app.commands.base import Command


class CommandInvoker:
    """Invoker for managing and executing commands in the REPL."""

    def __init__(self):
        """Initialize an empty command registry."""
        self._commands: Dict[str, Type[Command]] = {}

    def register_command(self, name: str, command: Type[Command]):
        """Register a new command."""
        self._commands[name] = command

    def execute_command(self, name: str, *args):
        """Execute a registered command synchronously."""
        command_class = self._commands.get(name)
        if not command_class:
            print("Unknown command. Type 'menu' to see available commands.")
            return

        command_instance = command_class()
        result = command_instance.execute(*args)
        print(f"Result: {result}")

    def execute_command_async(self, name: str, *args):
        """Execute a registered command asynchronously using multiprocessing."""
        if name not in self._commands:
            print("Unknown command. Type 'menu' to see available commands.")
            return

        process = multiprocessing.Process(target=self.execute_command, args=(name, *args))
        process.start()
        process.join()

    def get_available_commands(self):
        """Return a list of registered command names."""
        return list(self._commands.keys())
