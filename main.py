import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from Tools import music_play, log
from config import *
from test import test_log

logger = log.logger

logger.info('PiProjects Initiating...')
logger.info('Position 0 ')
BlockScheduler = BlockingScheduler()
BackScheduler = BackgroundScheduler()
logger.info('Position 1')
BackScheduler._logger = logger
logger.info('Position 2')
BlockScheduler._logger = logger
logger.info('Position 3')
# time.sleep(100)
# logger.info('Sleep Finished.')
# music_play.random_play('musics')
# logger.info('PiProjects Scheduler StartUp!')
BlockScheduler.add_job(func=music_play.random_play, args=('musics',), trigger='cron', max_instances=10, month='*',
                       day='*', hour='6', minute='45')
logger.info('Position 4')
# BlockScheduler.add_job(func=test_log, trigger='cron', max_instances=10, second='*/5')
logger.info('Position 5')
BackScheduler.start()
logger.info('Position 6')
BlockScheduler.start()
