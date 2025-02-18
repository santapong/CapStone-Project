import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.getLogger(__name__)

LOG_PATH = os.getenv('LOG_PATH', 'app.log')  # Default log path
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # Default log level
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Default format

def setup_logging():
    """ Configure the logging system for the application. """
    # Set up logging configuration
    logging.basicConfig(
        level=LOG_LEVEL,  # Set logging level (INFO, DEBUG, etc.)
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_PATH),  # Write logs to a file
            logging.StreamHandler()  # Optional: log to console as well
        ]
    )
    logging.info("Logging initialized successfully.")

    # Suppress unwanted log messages from specific libraries like watchfiles
    logging.getLogger("watchfiles.main").setLevel(logging.WARNING)