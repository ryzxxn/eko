import logging

def get_logger(name: str):
    """Returns a logger with a detailed debugging format."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Formatter with timestamp, file, function, and line number
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
