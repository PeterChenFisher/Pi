from . import log
import socket
import threading
import time

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432  # 监听的端口 (非系统级的端口: 大于 1023)
logger = log.logger


def wait_signal_and_run(events_to_run):
    logger.info('正在判斷信號是否為True。。。')
    while True:
        time.sleep(1)
        for func in events_to_run:
            if events_to_run[func][1] is True:
                logger.info(f'将运行： {func}')
                func_th = threading.Thread(target=func)
                func_th.start()
                events_to_run[func][1] = False


def socket_wait(events_to_run):
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
                for key, value in events_to_run.items():
                    if data.decode() == value[0]:
                        events_to_run[key][1] = True
                logger.info(f'Received: {data}.')
                conn.sendall(b'Datas Received!Thanks!')

# if __name__ == '__main__':
#     show_sig_th = threading.Thread(target=wait_signal_and_run)
#     show_sig_th.start()
# socket_wait()
