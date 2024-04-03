import logging


def get_logger(name: str, log_level: int = logging.INFO, formatter: str = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    if formatter:
        formatter = logging.Formatter(formatter)
        console_handler.setFormatter(formatter)
    else:
        default_formatter = logging.Formatter('%(levelname)s:\t  %(message)s - %(name)s:%(lineno)d [%(asctime)s]')
        console_handler.setFormatter(default_formatter)

    logger.addHandler(console_handler)
    return logger
