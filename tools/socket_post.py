import time
import socket

HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
PORT = 65432  # 服务器使用的端口


def socket_post(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            s.sendall(b'random_play')
            data = s.recv(1024)
            if data == 'False':
                break
            time.sleep(5)

    print('Received', repr(data))

