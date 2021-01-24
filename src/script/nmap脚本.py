#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nmap
# import sys

def nmap_ping_scan(network_prefix : str):
    """ping扫描活动主机"""
    nm = nmap.PortScanner()
    ping_scan_raw_result = nm.scan(hosts=network_prefix, ports=None, arguments='-v -n -sn', sudo=False)
    host_list = []

    # 分析扫描结果，放入清单
    for result in  ping_scan_raw_result['scan'].values():
        if result['status']['state'] == 'up':
            host_list.append(result['addresses']['ipv4'])
    return host_list

if __name__ == '__main__':
    print('请输入要扫描的端口号：格式如 10.113.248.190-300 or 10.113.249.1-1000')
    hosts = input()
    for host in nmap_ping_scan(hosts[1]):
        print('%-20s %5s' % (host, 'is UP'))