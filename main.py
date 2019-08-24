import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from Tools import music_play, log
from config import *
from test import test_log

logger = log.logger

logger.info('PiProjects Initiating...')
BlockScheduler = BlockingScheduler()
BackScheduler = BackgroundScheduler()
BackScheduler._logger = logger
BlockScheduler._logger = logger
logger.info('PiProjects Scheduler StartUp!')
# Welcome!
music_play.random_play('musics')
BlockScheduler.add_job(func=music_play.random_play, args=('musics',), trigger='cron', max_instances=10, month='*',
                       day='*', hour='6', minute='45')
BackScheduler.start()
BlockScheduler.start()
