# /bin/env python
# -*-coding:utf-8-*-
import socket
import time

from . import log

logger = log.logger


# 检查网络连同性
def wait_network_on():
    if_network_on = False
    logger.info('Checking Network...')
    times = 0
    while True:
        remote_server = "www.baidu.com"
        try:
            # see if we can resolve the host name -- tells us if there is a DNS listening
            host = socket.gethostbyname(remote_server)
            s = socket.create_connection((host, 80), 2)
            if_network_on = True
            logger.info('NetWork Connected!!!')
            s.close()
            return if_network_on
        except Exception as e:
            times += 1
            if times % 20 == 0:
                logger.info(f'NetWork Disconnected... {e}')
        time.sleep(5)


# 获得本级制定接口的ip地址
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr
