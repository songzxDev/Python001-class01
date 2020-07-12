# -*- coding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

import time

import socket

socket.setdefaulttimeout(4)


def my_ping(param):
    ip, port = param
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sk.connect((ip, port))
        sk.shutdown(2)
        print('\033[1;32m.... is OK.\033[0m')
        return True

    except socket.timeout:
        print('\033[1;33m.... is down or network time out!!!\033[0m')
        return False
    except Exception as ex:
        print(ex)
        print('\033[1;31m.... is down!!!\033[0m')
        return False


if __name__ == "__main__":
    seed = [("192.168.1.19", i) for i in range(1, 100)]
    with ThreadPoolExecutor(3) as executor2:
        executor2.map(my_ping, seed)
