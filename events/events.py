from tools import ip_update, DDingWarn, socket_wait, log
import threading
from Spiders import jdjzww_daily

logger = log.logger


def initiator():
    # 程序初始化：初始时候需要启动的线程和任务
    starting_up()
    # wait_sig_and_check()
    return


def send_ip_address_to_dding():
    if ip_update.wait_network_on():
        ip_addr = ip_update.get_ip_address()
        message_result = [
            '你的树莓派IP地址是：',
            f'    {ip_addr}'
        ]
        DDingWarn.request_ding(result=message_result)
    return


def starting_up():
    ip_addr_report_threading = threading.Thread(target=send_ip_address_to_dding)
    ip_addr_report_threading.start()
    DDingWarn.request_ding(['你的石头派项目正在启动！'])
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
