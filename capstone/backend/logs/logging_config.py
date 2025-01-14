import logging
import os
from dotenv import load_dotenv

load_dotenv()

LOG_PATH = os.getenv('LOG_PATH')

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH),  # Write logs to a file
        ]
    )

    # Suppress logs from 'watchfiles' at INFO level
    logging.getLogger("watchfiles.main").setLevel(logging.WARNING)

# TODO: Make logs for database