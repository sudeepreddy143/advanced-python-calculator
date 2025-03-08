import cmd
from app.invoker import CommandInvoker

class CalculatorREPL(cmd.Cmd):
    intro = "Welcome to the Advanced Python Calculator. Type help or ? to list commands.\n"
    prompt = "(calc) "

    def __init__(self):
        super().__init__()
        self.invoker = CommandInvoker()

    def do_add(self, arg):
        """Add two numbers: add 2 3"""
        numbers = list(map(float, arg.split()))
        if len(numbers) != 2:
            print("Usage: add <num1> <num2>")
            return
        print(f"Result: {self.invoker.execute('add', *numbers)}")

    def do_exit(self, arg):
        """Exit the calculator"""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    CalculatorREPL().cmdloop()
