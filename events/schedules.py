from tools import ip_update, socket_wait, music_play
from .Oclock import time_report_morning_oclock
from events.Bibles import *
import threading
from . import LightBreath
from config import *

logger = log.logger
ip_addr = None
events_to_run = {
    music_play.random_play: ['random_play', False]
}


def initiator():
    # 程序初始化：初始时候需要启动的线程和任务
    DDingWarn.request_ding(['你的石头派项目正在启动！'])

    ip_addr_monitor_th = threading.Thread(target=ip_update.ip_addr_monitor)
    ip_addr_monitor_th.start()

    light_breath_th = threading.Thread(target=LightBreath.LightBreath, args=(11,))
    light_breath_th.start()

    wait_socket_th = threading.Thread(target=socket_wait.socket_wait, args=(events_to_run,))
    wait_socket_th.start()
    wait_sig_and_run_th = threading.Thread(target=socket_wait.wait_signal_and_run, args=(events_to_run,))
    wait_sig_and_run_th.start()


def add_block_schedule_jobs(BlockScheduler):
    # 周中早起闹钟音乐
    BlockScheduler.add_job(func=weekday_morning_oclock, trigger='cron', max_instances=10, month='*',
                           day_of_week='mon,tue,wed,thu,fri', hour='6', minute='40')
    # 周末早起闹钟音乐
    BlockScheduler.add_job(func=music_play.random_play, args=('musics', 'commandline', 10), trigger='cron',
                           max_instances=10, month='*', day_of_week='sat,sun', hour='8', minute='30')
    # 每天早上爬取灵修经文并推送到钉钉
    BlockScheduler.add_job(func=daily_scripture, trigger='cron', max_instances=10, month='*', day='*',
                           hour='6', minute='15')
    return


def add_back_schedule_jobs(BackScheduler):
    # # 整点提醒功能（每到整点播放纯音乐）
    # BackScheduler.add_job(func=music_play.random_play, args=(None, 'commandline', 1, pure_musics_mode), trigger='cron',
    #                       max_instances=10, month='*', day='*', hour='*', minute='00')
    # 每4天重置一次播放器中的音乐列表读取信号reload_sig，使播放器每4天重新获取一次音乐列表
    BackScheduler.add_job(func=music_play.reload_sig_state_switch, trigger='interval', days=4)
    return
