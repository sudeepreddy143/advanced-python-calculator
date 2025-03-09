import pandas as pd
import os

HISTORY_FILE = "history.csv"


class HistoryManager:
    @staticmethod
    def load():
        """Load history from CSV file."""
        if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
            return pd.DataFrame(columns=["operation", "operands", "result"])  # Return empty DataFrame

        try:
            df = pd.read_csv(HISTORY_FILE)
            return df if not df.empty else pd.DataFrame(columns=["operation", "operands", "result"])
        except (pd.errors.EmptyDataError, FileNotFoundError):
            return pd.DataFrame(columns=["operation", "operands", "result"])
        except Exception as e:
            raise RuntimeError(f"Error loading history: {e}")

    @staticmethod
    def save(operation, operands, result):
        """Save a calculation result to history."""
        new_entry = pd.DataFrame([{"operation": operation, "operands": str(operands), "result": result}])  
        # Ensures operands are saved as a string to avoid CSV format issues

        if os.path.exists(HISTORY_FILE) and os.stat(HISTORY_FILE).st_size > 0:
            try:
                df = pd.read_csv(HISTORY_FILE)
            except pd.errors.EmptyDataError:
                df = pd.DataFrame(columns=["operation", "operands", "result"])
        else:
            df = pd.DataFrame(columns=["operation", "operands", "result"])

        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(HISTORY_FILE, index=False)

    @staticmethod
    def clear():
        """Clear the entire history."""
        open(HISTORY_FILE, "w").close()

    @staticmethod
    def delete_last():
        """Delete the last entry from history."""
        if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
            return

        try:
            df = pd.read_csv(HISTORY_FILE)
            if df.empty:
                return
            df = df.iloc[:-1]  # Remove last row
            df.to_csv(HISTORY_FILE, index=False)
        except Exception as e:
            raise RuntimeError(f"Error deleting last entry: {e}")
