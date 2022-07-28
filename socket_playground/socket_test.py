import socket
from contextlib import closing


def is_socket_taken(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        connect_status_no = sock.connect_ex((host, port))
        if connect_status_no == 0:
            return True
        else:
            return False


is_socket_taken("127.0.0.1", 6666)