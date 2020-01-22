from . import log
import socket
import threading
import time

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432  # 监听的端口 (非系统级的端口: 大于 1023)
Signal = False
Message = ''
# TODO 设置接收到的信息为 b'message',接收到即检查该信号在信号仓库里是否有存在,若无，返回错误，
#  若有，将signal设置为True，并将变量Message更改；
#  signal信号检测函数检测到True，查询Message，执行相关函数。
logger = log.logger


def wait_signal_and_run(func):
    global signal

    logger.info('正在判斷信號是否為True。。。')
    while True:
        time.sleep(1)
        if signal is True:
            logger.info(f'Signal is: {signal}')
            func()
            time.sleep(5)
            signal = False


def socket_wait():
    global Signal

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        logger.info('Signal Socket is Listening...')
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                logger.info(f'Connected by{str(addr)}')
                data = conn.recv(1024)
                if data == b'True':
                    Signal = True
                logger.info(f'Received: {data}. Signal Status: {str(Signal)}')
                conn.sendall(b'Datas Received!Thanks!')


if __name__ == '__main__':
    show_sig_th = threading.Thread(target=wait_signal_and_run)
    show_sig_th.start()
    socket_wait()
