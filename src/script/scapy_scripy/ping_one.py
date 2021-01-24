#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import IP, UDP, ICMP


def scapy_ping_one(host):
    # 随机产生ip id位
    id_ip = randint(1, 65535)
    # 随机产生ping id位
    id_ping = randint(1, 65535)
    # 随机产生ping序列号位
    seq_ping = randint(1, 65535)

    # 构造ping数据包
    packet = IP(dst=host, ttl=1, id=id_ip)/ICMP(id=id_ping, seq=seq_ping)/b'hello'
    # 获取响应信息，超时2s，关闭详情信息
    ping_result = sr1(packet, timeout=2, verbose=False)
    # 如果有响应信息，退出码为3(默认退出码为0)
    if ping_result:
        ping_result.show()
        os._exit(3)

if __name__ == '__main__':
    scapy_ping_one(sys.argv[1])

def arp_spoof(target, ip2):
    pass

# 基本使用

# 发送arp包
# pkt = ARP()
# pkt.pdst='192.168.0.113'
#
# pkt.show()

# 接收回复
# result = srl(pkt)
# result.show()


# 发送ip包
# ip = IP(dst='192.168.2.11')
# 查看报文内容
# ls(ip)
