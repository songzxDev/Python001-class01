# -*- coding:utf-8 -*-
# 作业一：
# 背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，
# 探测目标主机是否开放了指定端口（1-1024），用于改善目标主机的安全状况。
# 要求：编写一个基于多进程或多线程模型的主机扫描器。
#
# 使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
# 使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
# IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
# 需考虑网络异常、超时等问题，增加必要的异常处理。
# 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
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
