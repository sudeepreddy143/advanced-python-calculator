"""
REPL for the Advanced Python Calculator.
Supports basic operations, history management, and plugins.
"""
import sys
from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.history import HistoryManager
from app.logging_config import logger
from app.invoker import CommandInvoker
from app.plugin_loader import load_plugins

COMMANDS = {
    "add": AddCommand(),
    "sub": SubtractCommand(),
    "mul": MultiplyCommand(),
    "div": DivideCommand(),
}

HISTORY_COMMANDS = ["history", "clear_history", "delete_last"]

# Ensure plugins load correctly
invoker = CommandInvoker()
load_plugins(invoker)

# ✅ Fix: Properly retrieve commands from `_commands` dictionary
COMMANDS.update(invoker._commands)  


def repl():
    """Runs the calculator REPL."""
    print("Welcome to Advanced Python Calculator (Type 'exit' to quit)")

    while True:
        try:
            command_line = input(">>> ").strip().lower()
            if not command_line:
                continue

            if command_line == "exit":
                sys.exit(0)

            if command_line == "menu":
                print("Available commands:", ", ".join(COMMANDS.keys()))
                print("History commands:", ", ".join(HISTORY_COMMANDS))
                continue

            if command_line in HISTORY_COMMANDS:
                handle_history_command(command_line)
                continue

            parts = command_line.split()
            command = parts[0]

            if command in COMMANDS:
                try:
                    args = list(map(float, parts[1:]))
                    result = COMMANDS[command].execute(*args)
                    print("Result:", result)
                    HistoryManager.save(command, str(args), result)

                except (ValueError, TypeError):
                    print("Invalid number of arguments.")
                    logger.error("Invalid number of arguments.")

            else:
                print("Unknown command. Type 'menu' for options.")

        except KeyboardInterrupt:
            print("\nExiting REPL.")
            sys.exit(0)
        except Exception as e:
            logger.error("Error: %s", e)
            print(f"Error: {e}")


def handle_history_command(command):
    """Handle history-related commands."""
    if command == "history":
        print(HistoryManager.load())
    elif command == "clear_history":
        HistoryManager.clear()
        print("History cleared.")
    elif command == "delete_last":
        HistoryManager.delete_last()
        print("Last history entry deleted.")


if __name__ == "__main__":
    repl()
