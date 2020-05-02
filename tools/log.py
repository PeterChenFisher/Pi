import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
import os
from config import *

logger = None
second_logger = None
third_logger = None


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


def set_logger(mode=None, second_log=None, third_log=None):
    global logger, second_logger, third_logger

    if mode is None or mode == Mode.Default:
        logger = logger_generator(logger_name='PeterPi', log_path=Mode.default_log_path)
    if mode == Mode.Assistant:
        logger = logger_generator(logger_name=mode, log_path=Mode.assistant_log_path)
    if mode == Mode.DailyScripture:
        logger = logger_generator(logger_name=mode, log_path=Mode.daily_scripture_log_path)

    if second_log:
        if mode == Mode.Assistant:
            second_logger = logger_generator(logger_name=mode, log_path=Mode.assistant_log_path)
        if mode == Mode.DailyScripture:
            second_logger = logger_generator(logger_name=mode, log_path=Mode.daily_scripture_log_path)

    if third_log:
        if mode == Mode.Assistant:
            third_logger = logger_generator(logger_name=mode, log_path=Mode.assistant_log_path)
        if mode == Mode.DailyScripture:
            third_logger = logger_generator(logger_name=mode, log_path=Mode.daily_scripture_log_path)

    return
