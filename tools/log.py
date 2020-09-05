import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
import os
from config import *

logger = None
second_logger = None
third_logger = None


def logger_generator(logger_name, when='midnight', log_path=None, logger=None):
    # init
    base_logger_path = log_path if log_path else os.path.join(excluded_file, 'log', logger_name)
    if not os.path.exists(os.path.join(excluded_file, 'log')):
        os.mkdir(os.path.join(excluded_file, 'log'))
    if not os.path.exists(base_logger_path):
        os.mkdir(base_logger_path)
    # create logger
    if not logger:
        logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        '[%(asctime)s] - [ %(name)s ] - %(levelname)s - %(message)s')
    if not logger.handlers:
        timedRotatingFileHandler = TimedRotatingFileHandler(filename=os.path.join(base_logger_path, logger_name),
                                                            when=when, interval=1, backupCount=60, encoding='utf-8')
        timedRotatingFileHandler.suffix = "%Y-%m-%d.log"
        timedRotatingFileHandler.setLevel(logging.INFO)
        timedRotatingFileHandler.setFormatter(formatter)

        streamHandler = StreamHandler()
        streamHandler.setLevel(logging.INFO)
        streamHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(timedRotatingFileHandler)
        logger.addHandler(streamHandler)

        logger.info(f'\n  StartUp Project {logger.name}.\n')
    return logger
