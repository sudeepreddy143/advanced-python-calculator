from app.commands.base import BaseCommand

class SquareCommand(BaseCommand):
    name = "square"
    
    def execute(self, x):
        return x * x
