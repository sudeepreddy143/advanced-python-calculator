"""
Handles history operations for the Advanced Python Calculator.
Uses CSV storage via Pandas.
"""
import os
import pandas as pd

HISTORY_FILE = "history.csv"


class HistoryManager:
    """Manages loading, saving, and clearing history."""

    @staticmethod
    def load():
        """Load history from CSV file."""
        if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
            return pd.DataFrame(columns=["operation", "operands", "result"])

        try:
            return pd.read_csv(HISTORY_FILE)
        except (pd.errors.EmptyDataError, FileNotFoundError):
            return pd.DataFrame(columns=["operation", "operands", "result"])
        except Exception as e:
            raise RuntimeError(f"Error loading history: {e}") from e

    @staticmethod
    def save(operation, operands, result):
        """Save a calculation result to history."""
        new_entry = pd.DataFrame([{"operation": operation, "operands": str(operands), "result": result}])

        df = HistoryManager.load()
        df = pd.concat([df, new_entry], ignore_index=True)

        df.to_csv(HISTORY_FILE, index=False)

    @staticmethod
    def clear():
        """Clear the entire history."""
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            file.truncate(0)

    @staticmethod
    def delete_last():
        """Delete the last entry from history."""
        df = HistoryManager.load()
        if df.empty:
            return

        df = df.iloc[:-1]  # Remove last row
        df.to_csv(HISTORY_FILE, index=False)
