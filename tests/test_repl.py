"""Test REPL behavior."""
import pytest
from unittest.mock import patch
from app.repl import repl

def test_repl_exit():
    """Test REPL exits correctly."""
    with patch("builtins.input", side_effect=["exit"]):
        with pytest.raises(SystemExit):
            repl()

def test_repl_menu(capsys):
    """Test REPL menu command."""
    with patch("builtins.input", side_effect=["menu", "exit"]):
        with pytest.raises(SystemExit):
            repl()
    
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
