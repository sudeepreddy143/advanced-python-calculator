"""Test history management."""
import os
import pytest
import pandas as pd
from app.history import HistoryManager

HISTORY_FILE = "test_history.csv"

@pytest.fixture(autouse=True)
def history_setup():
    """Setup test history file."""
    yield
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

def test_save_and_load():
    """Test saving and loading history."""
    HistoryManager.save("add", "(3, 2)", 5)
    history = HistoryManager.load()
    assert not history.empty
    assert history.iloc[-1]["operation"] == "add"

def test_clear_history():
    """Test clearing history."""
    HistoryManager.clear()
    history = HistoryManager.load()
    assert history.empty

def test_delete_last():
    """Test deleting the last entry."""
    HistoryManager.save("mul", "(4, 5)", 20)
    HistoryManager.delete_last()
    history = HistoryManager.load()
    assert history.empty
