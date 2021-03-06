# -*-coding:utf-8-*-
import socket
import time

from . import log
from . import DDingWarn

logger = log.logger
ip_addr = None


# 检查网络连接是否正常
def wait_network_on(limit=None):
    logger.info('Checking Network...')
    times = 0
    while True:
        if check_network_status():
            return True
        else:
            times += 1
            if times % 100 == 0:
                logger.info('NetWork Disconnected... ')
            if limit:
                if times > limit:
                    return False
            time.sleep(5)


def check_network_status():
    if_network_on = False
    remote_server = "www.baidu.com"
    try:
        # see if we can resolve the host name -- tells us if there is a DNS listening
        host = socket.gethostbyname(remote_server)
        s = socket.create_connection((host, 80), 2)
        if_network_on = True
        logger.info('NetWork Connected!!!')
        s.close()
        return if_network_on
    except:
        return if_network_on


# 获得本机指定接口的ip地址
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr


# IP 监控
def ip_addr_monitor():
    global ip_addr

    realtime_ipaddr = None
    while 1:
        if wait_network_on():
            realtime_ipaddr = get_ip_address()
        if ip_addr is None or ip_addr != realtime_ipaddr:
                ip_addr = realtime_ipaddr
                message_result = [
                    '你的树莓派IP地址是：',
                    f'    {ip_addr}'
                ]
                DDingWarn.request_ding(result=message_result)
        time.sleep(60 * 5)


def net_work_monitor():
    while 1:
        if not wait_network_on(limit=5):
            # TODO 点亮一颗LED红灯
            DDingWarn.request_ding(result=['网络失常'])
