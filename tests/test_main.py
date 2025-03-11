"""Test main entry point."""
import pytest
from unittest.mock import patch
from app.main import repl

def test_main_repl():
    """Test REPL starts without crashing."""
    with patch("builtins.input", side_effect=["exit"]):
        with pytest.raises(SystemExit):
            repl()
