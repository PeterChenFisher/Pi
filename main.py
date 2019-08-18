from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from Tools import music_play

if __name__ == '__main__':
    BlockScheduler = BlockingScheduler()
    BackScheduler = BackgroundScheduler()
    BlockScheduler.add_job(func=music_play.random_play, args=('musics',), trigger='cron', max_instances=10, month='*',
                           day='*', hour='6', minute='45')
    BlockScheduler.start()
    BackScheduler.start()
