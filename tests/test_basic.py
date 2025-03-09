import pytest
from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add():
    assert AddCommand().execute(3, 2) == 5

def test_subtract():
    assert SubtractCommand().execute(3, 2) == 1

def test_multiply():
    assert MultiplyCommand().execute(3, 2) == 6

def test_divide():
    assert DivideCommand().execute(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        DivideCommand().execute(6, 0)
