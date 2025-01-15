import logging
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

logging.getLogger(__name__)

""" TODO: Make it will read from toml file.
#################################################################################################
#                                       Logging Note                                            #
#  LOGGING Level in default is "INFO" you can config in .env of your                            #
#  LOGGING Format in default is "%(asctime)s - %(name)s - %(levelname)s - %(message)s"          #
#                                                                                               #           
#  :See more https://docs.python.org/3/library/logging.html#logging-levels                      #
#                                                                                               #
#################################################################################################
"""

LOG_PATH = os.getenv('LOG_PATH')

# TODO: Make log level will work with any level.
LOG_LEVEL = os.getenv("LOG_LEVEL")
LOG_FORMAT = os.getenv('LOG_FORMAT')

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_PATH),  # Write logs to a file
        ]
    )
    logging.info("Intial logs")

    # Suppress logs from 'watchfiles' at INFO level
    logging.getLogger("watchfiles.main").setLevel(logging.WARNING)

# TODO: Make logs for database

# Intial Log
setup_logging()