import socket

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432  # 监听的端口 (非系统级的端口: 大于 1023)

signal = False


def socket_wait():
    global signal

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if data is True:
                    signal = True
                conn.sendall(data)
