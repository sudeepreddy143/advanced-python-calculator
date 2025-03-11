"""Logging configuration for the Advanced Python Calculator."""
import logging
import os

# Ensure logs directory exists
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)

# Set log level from environment variable (default: INFO)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

if LOG_LEVEL not in VALID_LEVELS:
    LOG_LEVEL = "INFO"

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("app")
logger.info("Logging initialized with level: %s", LOG_LEVEL)
