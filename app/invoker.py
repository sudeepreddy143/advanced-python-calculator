from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CommandInvoker:
    def __init__(self):
        self.commands = {
            "add": AddCommand,
            "subtract": SubtractCommand,
            "multiply": MultiplyCommand,
            "divide": DivideCommand,
        }

    def execute(self, name, *args):
        if name in self.commands:
            return self.commands[name](*args).execute()
        else:
            return f"Unknown command: {name}"
