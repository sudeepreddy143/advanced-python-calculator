import os
import pandas as pd
from app.history import HistoryManager

def test_history():
    history = HistoryManager()
    history.save_to_history("add", ["3", "5"], "8")

    df = pd.read_csv("history.csv")
    assert not df.empty

    history.clear_history()
    df = pd.read_csv("history.csv")
    assert df.empty
