from app.commands.base import BaseCommand

COMMAND_NAME = "power"

class PowerCommand(BaseCommand):
    """Exponentiation Command."""
    def execute(self, x, y):
        return x ** y
