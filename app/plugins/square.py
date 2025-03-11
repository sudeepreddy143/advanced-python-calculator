from app.commands.base import BaseCommand

COMMAND_NAME = "square"

class SquareCommand(BaseCommand):
    """Square Command (only takes one argument)."""
    def execute(self, x):
        return x * x
