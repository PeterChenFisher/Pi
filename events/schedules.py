from tools import music_play, DDingWarn
from config import *
from .events import *
from Spiders import jdjzww_daily


def add_block_schedule_jobs(BlockScheduler):
    # 周中早起闹钟音乐
    BlockScheduler.add_job(func=music_play.random_play, args=(None, 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='mon,tue,wed,thu,fri', hour='6', minute='30')
    # 周末早起闹钟音乐
    BlockScheduler.add_job(func=music_play.random_play, args=('musics', 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='sat,sun', hour='8', minute='30')
    # 每天早上爬取灵修经文并推送到钉钉
    BlockScheduler.add_job(func=jdjzww_daily.daily_scripture, trigger='cron', max_instances=10, month='*', day='*',
                           hour='6', minute='15')
    return


def add_back_schedule_jobs(BackScheduler):
    # 每晚十一点报晚安
    # BackScheduler.add_job(func=DDingWarn.request_ding, args=([heart_beat_text2],), trigger='cron',
    #                       max_instances=10, month='*', day='*', hour='23', minute='00')
    # 整点提醒功能（每到整点播放纯音乐）
    BackScheduler.add_job(func=music_play.random_play, args=(None, 'commandline', 1, pure_music), trigger='cron',
                          max_instances=10, month='*', day='*', hour='*', minute='00')
    # 每4天重置一次播放器中的音乐列表读取信号reload_sig，使播放器每4天重新获取一次音乐列表
    BackScheduler.add_job(func=music_play.reload_sig_state_switch, trigger='interval', days=4)
    return
