"""Test plugin loader."""
import pytest
from app.plugin_loader import load_plugins
from app.invoker import CommandInvoker

def test_load_plugins():
    """Ensure plugins are loaded correctly."""
    invoker = CommandInvoker()
    load_plugins(invoker)

    available_commands = invoker.get_available_commands()
    assert "power" in available_commands, "Power plugin was not loaded"
    assert "square" in available_commands, "Square plugin was not loaded"
