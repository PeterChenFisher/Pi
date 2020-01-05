from . import log
import socket
import threading
import time

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432  # 监听的端口 (非系统级的端口: 大于 1023)
Signal = False

logger = log.logger


def show_signal():
    global Signal
    while True:
        time.sleep(1)
        if Signal is True:
            logger.info(f'Signal is: {str(Signal)}')
            time.sleep(1)
            Signal = False


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
    show_sig_th = threading.Thread(target=show_signal)
    show_sig_th.start()
    socket_wait()
