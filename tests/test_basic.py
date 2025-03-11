"""Test basic arithmetic commands."""
import pytest
from app.commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.mark.parametrize("x, y, expected", [(10, 5, 15), (3, 3, 6), (-2, 2, 0)])
def test_add(x, y, expected):
    """Test addition command."""
    command = AddCommand()
    assert command.execute(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [(10, 5, 5), (3, 3, 0), (-2, 2, -4)])
def test_subtract(x, y, expected):
    """Test subtraction command."""
    command = SubtractCommand()
    assert command.execute(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [(10, 5, 50), (3, 3, 9), (-2, 2, -4)])
def test_multiply(x, y, expected):
    """Test multiplication command."""
    command = MultiplyCommand()
    assert command.execute(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [(10, 5, 2), (9, 3, 3), (2, 4, 0.5)])
def test_divide(x, y, expected):
    """Test division command."""
    command = DivideCommand()
    assert command.execute(x, y) == expected

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        command.execute(5, 0)
