import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    filename="logs/app.log",
    level=LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

logger = logging.getLogger(__name__)
