import logging
from app.repl import REPL
from app.logger import setup_logging
from app.database import Database

if __name__ == "__main__":
    setup_logging()
    logging.info("Starting the Advanced Python Calculator...")
    database = Database()
    repl = REPL(database)
    repl.run()
