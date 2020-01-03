import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
import os
import config


def logger_generator(log_path, logger_name, when='midnight', logger=None):
    # init
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    # create logger
    if not logger:
        logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        '[%(asctime)s] - [ %(name)s ] - %(levelname)s - %(message)s')

    timedRotatingFileHandler = TimedRotatingFileHandler(filename=os.path.join(log_path, logger_name), when=when,
                                                        interval=1, backupCount=60, encoding='utf-8')
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


logger = logger_generator(logger_name='PeterPi', log_path=config.log_path)
