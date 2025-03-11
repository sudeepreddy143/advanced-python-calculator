"""Main entry point for the Advanced Python Calculator."""
from app.repl import repl
from app.logging_config import logger

if __name__ == "__main__":
    logger.info("Starting the Advanced Python Calculator...")
    try:
        repl()
    except Exception as e:
        logger.error("Application encountered an error: %s", e)
