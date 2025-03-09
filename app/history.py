import pandas as pd
import os

HISTORY_FILE = "history.csv"


class HistoryManager:
    @staticmethod
    def load():
        """Load history from CSV file."""
        if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
            return "No history found."

        try:
            df = pd.read_csv(HISTORY_FILE)
            if df.empty:
                return "No history found."
            return df
        except pd.errors.EmptyDataError:
            return "No history found."
        except Exception as e:
            return f"Error loading history: {e}"

    @staticmethod
    def save(operation, operands, result):
        """Save a calculation result to history."""
        new_entry = {"operation": operation, "operands": operands, "result": result}

        if os.path.exists(HISTORY_FILE) and os.stat(HISTORY_FILE).st_size > 0:
            try:
                df = pd.read_csv(HISTORY_FILE)
            except pd.errors.EmptyDataError:
                df = pd.DataFrame(columns=["operation", "operands", "result"])
        else:
            df = pd.DataFrame(columns=["operation", "operands", "result"])

        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(HISTORY_FILE, index=False)

    @staticmethod
    def clear():
        """Clear the entire history."""
        open(HISTORY_FILE, "w").close()

    @staticmethod
    def delete_last():
        """Delete the last entry from history."""
        if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
            return "No history to delete."

        try:
            df = pd.read_csv(HISTORY_FILE)
            if df.empty:
                return "No history to delete."
            df = df[:-1]  # Remove last row
            df.to_csv(HISTORY_FILE, index=False)
        except Exception as e:
            return f"Error deleting last entry: {e}"
