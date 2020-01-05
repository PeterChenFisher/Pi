from tools import ip_update, DDingWarn
import threading
import projects


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
    ip_addr_report_threading = threading.Thread(target=send_ip_address_to_dding)
    ip_addr_report_threading.start()
    DDingWarn.request_ding(['你的石头派项目正在启动！'])
    return


def initiator():
    # 程序初始化：初始时候需要启动的线程和任务
    starting_up()
    return
