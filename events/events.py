from tools import ip_update, DDingWarn
import threading


def send_ip_address_to_dding():
    if ip_update.wait_network_on():
        ip_addr = ip_update.get_ip_address()
        message_result = [
            '你的树莓派IP地址是：',
            ip_addr
        ]
        DDingWarn.request_ding(result=message_result)
    return


def starting_up():
    th = threading.Thread(target=send_ip_address_to_dding)
    th.start()
    return


def initiator():

    return
