import logging


class CustomFormatter(logging.Formatter):

    c = "\x1b[36;21m"
    g = "\x1b[32;21m"
    y = "\x1b[33;21m"
    r = "\x1b[31;21m"
    b = "\x1b[34;21m"

    bold = "\033[1m"
    end = "\x1b[0m"

    level_name = "%(levelname)s"
    name = "%(name)s:%(lineno)d"
    message = "%(message)s"
    asctime = "%(asctime)s"

    ind = ":\t  "
    hyp = " - "
    ob = " ["
    cb = "] "

    level_name = level_name + end
    message = bold + message + end
    asctime = ob + c + asctime + end + cb

    constructor = level_name + ind + name + hyp + message + asctime

    FORMATS = {
        logging.DEBUG: b + constructor,
        logging.INFO: g + constructor,
        logging.WARNING: y + constructor,
        logging.ERROR: r + constructor,
        logging.CRITICAL: r + bold + constructor,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name: str, log_level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(CustomFormatter())

    logger.addHandler(console_handler)
    return logger
