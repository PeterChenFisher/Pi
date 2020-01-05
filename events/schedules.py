from tools import music_play, DDingWarn
from events import heart_beats
import config


def add_block_schedule_jobs(BlockScheduler):
    BlockScheduler.add_job(func=music_play.random_play, args=('musics', 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='mon,tue,wed,thu,fri', hour='6', minute='45')
    BlockScheduler.add_job(func=music_play.random_play, args=('musics', 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='sat,sun', hour='8', minute='30')
    return


def add_back_schedule_jobs(BackScheduler):
    BackScheduler.add_job(func=DDingWarn.request_ding, args=([config.heart_beat_text2],), trigger='cron',
                          max_instances=10, month='*', day='*', hour='23', minute='00')
    BackScheduler.add_job(func=heart_beats.TimeReporting, trigger='cron', max_instances=10, month='*', day='*',
                          hour='*', minute='00')
    BackScheduler.add_job(func=heart_beats.TimeReporting, trigger='cron', max_instances=10, month='*', day='*',
                          hour='*', minute='30')
    # BackScheduler.add_job(func=DDingWarn.request_ding, args=([config.heart_beat_text2],), trigger='cron',
    #                       max_instances=10,
    #                       month='*', day_of_week='sat,sun', hour='8', minute='49')
    # BackScheduler.add_job(func=DDingWarn.request_ding, args=([config.heart_beat_text2],), trigger='cron',
    #                       max_instances=10,
    #                       month='*', day_of_week='mon,tue,wed,thu,fri', hour='6', minute='45')
    return
