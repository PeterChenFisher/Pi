import time
from tools import ip_update, DDingWarn, socket_wait, log, music_play
import threading
from . import LightBreath
from Spiders import jdjzww_daily
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

    light_breath_th = threading.Thread(target=LightBreath.LightBreath(light_code=11))
    light_breath_th.start()

    wait_socket_th = threading.Thread(target=socket_wait.socket_wait, args=(events_to_run,), daemon=True)
    wait_socket_th.start()
    wait_sig_and_run_th = threading.Thread(target=socket_wait.wait_signal_and_run, args=(events_to_run,), daemon=True)
    wait_sig_and_run_th.start()
