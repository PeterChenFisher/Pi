import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from Tools import music_play, log
from config import *

logger = log.logger

if __name__ == '__main__':
    BlockScheduler = BlockingScheduler()
    BackScheduler = BackgroundScheduler()
    BackScheduler._logger = logger
    BlockScheduler._logger = logger
    time.sleep(100)

    music_play.random_play('musics')
    BlockScheduler.add_job(func=music_play.random_play, args=('musics',), trigger='cron', max_instances=10, month='*',
                           day='*', hour='6', minute='45')
    BackScheduler.start()
    BlockScheduler.start()
