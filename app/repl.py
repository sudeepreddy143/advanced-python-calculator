import sys
from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.history import HistoryManager
from app.logging_config import logger

COMMANDS = {
    "add": AddCommand(),
    "sub": SubtractCommand(),
    "mul": MultiplyCommand(),
    "div": DivideCommand(),
}

HISTORY_COMMANDS = ["history", "clear_history", "delete_last"]


def repl():
    """Runs the calculator REPL."""
    print("Welcome to Advanced Python Calculator (Type 'exit' to quit)")

    while True:
        try:
            command_line = input(">>> ").strip().lower()
            if not command_line:
                continue  # Ignore empty input

            if command_line == "exit":
                break

            elif command_line == "menu":
                print("Available commands:", ", ".join(COMMANDS.keys()))
                print("History commands:", ", ".join(HISTORY_COMMANDS))

            elif command_line == "history":
                print(HistoryManager.load())  # ✅ Show history

            elif command_line == "clear_history":
                HistoryManager.clear()  # ✅ Clear history
                print("History cleared.")

            elif command_line == "delete_last":
                HistoryManager.delete_last()  # ✅ Delete last history entry
                print("Last history entry deleted.")

            else:
                parts = command_line.split()

                # Check if command is a valid math operation with two numbers
                if len(parts) == 3 and parts[0] in COMMANDS:
                    try:
                        x, y = float(parts[1]), float(parts[2])
                        result = COMMANDS[parts[0]].execute(x, y)
                        print("Result:", result)

                        # ✅ Save result to history
                        HistoryManager.save(parts[0], f"({x}, {y})", result)

                    except ValueError:
                        print("Invalid input. Please enter valid numbers.")
                else:
                    print("Unknown command. Type 'menu' for options.")

        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")


if __name__ == "__main__":
    repl()
