#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 日志
import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

import ipaddress
import time
import multiprocessing
from scapy.all import *
from src.script.scapy_scripy.ping_one import scapy_ping_one


def scapy_ping_scan(network):
    net = ipaddress.ip_network(network)
    ip_processes = {}
    ip_list = []
    for ip in net:
        # 读取网络中的每一个ip地址,特殊的ip类转字符串
        ip_addr = str(ip)
        # 多进程
        ping_one = multiprocessing.Process(target=scapy_ping_one, args=(ip_addr, ))
        ping_one.start()
        ip_processes[ip_addr] = ping_one

    for ip, process in ip_processes.items():
        # 判断进程退出码表示为ping成功
        if process.exitcode == 3:
            ip_list.append(ip)
        else:
            process.terminate()
    return sorted(ip_list)

if __name__ == '__main__':
    print('请输入network：格式如 10.113.248.0/24')
    hosts = input()
    t1 = time.time()
    active_up = scapy_ping_scan(hosts)
    print('活动ip地址如下：')
    for ip in active_up:
        print(ip)
    t2 = time.time()
    print(t2-t1)