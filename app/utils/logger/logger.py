import logging

from core.config import settings
from utils.logger.custom_formatter import CustomFormatter


def get_logger(name: str, log_level: int = settings.LOGGING_LEVEL) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(CustomFormatter())

    logger.addHandler(console_handler)
    return logger
