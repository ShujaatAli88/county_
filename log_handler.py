import os
import sys
from loguru import logger
from constants import DATA_DIRECTORY, LOGS_FILE_NAME

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level><cyan>{level: <8}</cyan></level> | "
    "<magenta>{name}</magenta>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - "
    "<level><green>{message}</green></level>"  # <-- This makes the message green for INFO logs
)

class LogHandler:
    def __init__(self, logs_file_path: str) -> None:
        if os.path.exists(logs_file_path):
            os.remove(logs_file_path)
        logger.remove()
        self.logs_file_path = logs_file_path
        self.logger = logger
        logger.add(logs_file_path)
        logger.add(sys.stderr, format=LOG_FORMAT, colorize=True)


LOGS_FILE_PATH = os.path.join(DATA_DIRECTORY, LOGS_FILE_NAME)
_logger = LogHandler(LOGS_FILE_PATH).logger

## example usage
# from log_handler import _logger
# _logger.info("Test Log")