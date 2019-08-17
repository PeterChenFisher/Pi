import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from Oclock import random_play

if __name__ == '__main__':
    BlockScheduler = BlockingScheduler()
    BackScheduler = BackgroundScheduler()
    BlockScheduler.add_job(func=random_play.random_play, args=('musics',), trigger='cron', max_instances=10, month='*',
                           day='*', hour='20', minute='34')
    BlockScheduler.start()
    BackScheduler.start()
