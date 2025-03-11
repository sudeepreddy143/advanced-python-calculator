"""Test plugins."""
from app.plugins.power import PowerCommand
from app.plugins.square import SquareCommand

def test_power():
    """Test power command."""
    command = PowerCommand()
    assert command.execute(2, 3) == 8

def test_square():
    """Test square command."""
    command = SquareCommand()
    assert command.execute(4) == 16
