import logging

def get_logger():
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.addHandler(logging.FileHandler('todo.log'))
    return logger