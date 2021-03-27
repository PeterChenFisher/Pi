import threading

from config import *
from events import heart_beats, LightBreath
from tools import DDingWarn, log, music_play, reformat_music_type, Text2Speech
from .Oclock import time_report_morning_clock

logger = log.logger
ip_addr = None


# 程序初始化：初始时候需要启动的线程和任务
def initiator(logger_name):
    DDingWarn.logger = log.logger_generator(logger_name=logger_name)
    music_play.logger = log.logger_generator(logger_name=logger_name)
    heart_beats.logger = log.logger_generator(logger_name=logger_name)
    Text2Speech.logger = log.logger_generator(logger_name=logger_name)

    DDingWarn.request_ding(['你的音乐闹钟项目正在启动！'])

    light_breath_th = threading.Thread(target=LightBreath.LightBreath, args=(11,))
    light_breath_th.start()


def add_block_schedule_jobs(BlockScheduler):
    # 周中早起闹钟音乐
    BlockScheduler.add_job(func=time_report_morning_clock, trigger='cron', max_instances=10, month='*',
                           day_of_week='mon,tue,wed,thu,fri', hour='6', minute='40')
    # BlockScheduler.add_job(func=time_report_morning_clock, trigger='cron', max_instances=10, month='*',
    #                        day_of_week='sun', hour='6', minute='40')
    # 周末早起闹钟音乐
    BlockScheduler.add_job(func=music_play.random_play, args=('musics', 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='sat,sun', hour='08', minute='30')
    # 每天晚上十点半播放纯音乐-《使命》
    BlockScheduler.add_job(func=music_play.pi_mplayer, args=('musics/使命.mp3',), trigger='cron',
                           max_instances=10, month='*', hour='22', minute='30')
    BlockScheduler.add_job(func=music_play.pi_mplayer, args=('musics/直到主耶稣再来时候.mp3',), trigger='cron',
                           max_instances=10, month='*', hour='23', minute='00')
    return


def add_back_schedule_jobs(BackScheduler):
    # # 整点提醒功能（每到整点播放纯音乐）
    # BackScheduler.add_job(func=music_play.random_play, args=(None, 'commandline', 1, pure_musics_mode), trigger='cron',
    #                       max_instances=10, month='*', day='*', hour='*', minute='00')
    # 每4天重置一次播放器中的音乐列表读取信号reload_sig，使播放器每4天重新获取一次音乐列表
    BackScheduler.add_job(func=music_play.reload_sig_state_switch, trigger='interval', days=4)
    # 每2天，将音乐txt文件更新为直链播放json文件
    BackScheduler.add_job(func=reformat_music_type.reformat_cloud_musics, trigger='interval', days=2)
    # 每2天自动拉取更新代码
    BackScheduler.add_job(func=os.system, args=(f'bash {ProjAutomationUpdateBashFile}',), trigger='interval', days=1)
    return
