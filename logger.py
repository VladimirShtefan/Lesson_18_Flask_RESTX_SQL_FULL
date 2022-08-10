import logging


def create_logger(name: str) -> logging.Logger:
    file_formatter = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s] %(message)s')

    file_debug_handler = logging.FileHandler('debug_log.log')
    file_error_handler = logging.FileHandler('errors_log.log')

    file_debug_handler.setLevel(logging.DEBUG)
    file_error_handler.setLevel(logging.ERROR)

    file_debug_handler.setFormatter(file_formatter)
    file_error_handler.setFormatter(file_formatter)

    logger = logging.getLogger(name)

    logger.addHandler(file_debug_handler)
    logger.addHandler(file_error_handler)
    logger.setLevel(logging.DEBUG)

    return logger
