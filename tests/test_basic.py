import pytest
from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    assert AddCommand(2, 3).execute() == 5

def test_subtract_command():
    assert SubtractCommand(10, 4).execute() == 6

def test_multiply_command():
    assert MultiplyCommand(3, 5).execute() == 15

def test_divide_command():
    assert DivideCommand(10, 2).execute() == 5
    assert DivideCommand(10, 0).execute() == "Error: Division by zero"
