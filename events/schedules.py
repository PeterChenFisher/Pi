from tools import music_play, DDingWarn
from events import heart_beats
from config import *


def add_block_schedule_jobs(BlockScheduler):
    # 周中早起闹钟音乐
    BlockScheduler.add_job(func=music_play.random_play, args=(None, 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='mon,tue,wed,thu,fri', hour='7', minute='45')
    # 周末早起闹钟音乐
    BlockScheduler.add_job(func=music_play.random_play, args=('musics', 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='sat,sun', hour='8', minute='30')
    return


def add_back_schedule_jobs(BackScheduler):
    # 每晚十一点报晚安
    BackScheduler.add_job(func=DDingWarn.request_ding, args=([heart_beat_text2],), trigger='cron',
                          max_instances=10, month='*', day='*', hour='23', minute='00')
    # 整点提醒功能（每到整点自动报时）
    BackScheduler.add_job(func=music_play.random_play, args=(None, 'commandline', 1, pure_music), trigger='cron',
                          max_instances=10, month='*', day='*', hour='*', minute='00')
    return
