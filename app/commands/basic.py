from .base import BaseCommand

class AddCommand(BaseCommand):
    """Addition Command."""
    name = "add"

    def execute(self, x, y):
        return x + y

class SubtractCommand(BaseCommand):
    """Subtraction Command."""
    name = "sub"

    def execute(self, x, y):
        return x - y

class MultiplyCommand(BaseCommand):
    """Multiplication Command."""
    name = "mul"

    def execute(self, x, y):
        return x * y

class DivideCommand(BaseCommand):
    """Division Command."""
    name = "div"

    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
