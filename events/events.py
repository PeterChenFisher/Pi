import time
from tools import ip_update, DDingWarn, socket_wait, log
import threading
from Spiders import jdjzww_daily
from config import *

logger = log.logger
ip_addr = None


def initiator():
    # 程序初始化：初始时候需要启动的线程和任务
    DDingWarn.request_ding(['你的石头派项目正在启动！'])
    ip_addr_monitor_th = threading.Thread(target=ip_update.ip_addr_monitor)
    ip_addr_monitor_th.start()
    # gpio_tool.gpio_init()
    return


def wait_sig_and_check(func_to_run):
    wait_socket_th = threading.Thread(target=socket_wait.socket_wait, daemon=True)
    wait_socket_th.start()
    wait_sig_and_run_th = threading.Thread(target=socket_wait.wait_signal_and_run, args=(func_to_run,), daemon=True)
    wait_sig_and_run_th.start()
    return


def daily_scripture():
    logger.info(f'开始爬取每日经文...')
    jdjzww_daily.update_url_list()
    scripture = jdjzww_daily.get_very_day_scripture()
    logger.info('今日经文请求钉钉！')
    DDingWarn.request_ding(result=[str(scripture)])
    logger.info(f'爬取每日经文结束。')
    return
