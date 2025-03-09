from app.commands.base import BaseCommand

class PowerCommand(BaseCommand):
    name = "power"
    
    def execute(self, x, y):
        return x ** y
