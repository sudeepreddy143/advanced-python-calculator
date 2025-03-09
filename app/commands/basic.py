from .base import BaseCommand

class AddCommand(BaseCommand):
    name = "add"
    
    def execute(self, x, y):
        return x + y

class SubtractCommand(BaseCommand):
    name = "sub"
    
    def execute(self, x, y):
        return x - y

class MultiplyCommand(BaseCommand):
    name = "mul"
    
    def execute(self, x, y):
        return x * y

class DivideCommand(BaseCommand):
    name = "div"
    
    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
