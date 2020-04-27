#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from config.path import binPath
from src.utils.Log import log

class timer():
    def __init__(self,startTime="09:00"):
        self.startTime = startTime
        self.log = log()

    def timerExecute(self,executeTask="executeTask"):
        while True:
            now = time.strftime("%H:%M",time.localtime())
            if now == self.startTime:
                try:
                    self.log.info("开始执行测试任务")
                    print("开始执行测试任务")
                    os.chdir(binPath())
                    os.system("python " + executeTask + ".py")
                    self.log.info("测试任务执行完毕")
                    #print("测试任务执行完毕")
                    break
                except:
                    self.log.info("执行测试任务失败")
                    #print("启动测试任务失败")
            else:
                time.sleep(1)
                print(now)

if __name__ == '__main__':
    # input_time = str(input("请输入开始时间"))
    # start = timer()
    # start.timerExecute()
    # 字符类型的时间
    tss1 = '2013-10-10 23:40:00'
    # 转为时间数组
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    print(timeArray)
    # timeArray可以调用tm_year等
    print(timeArray.tm_year)   # 2013
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(type(timeStamp))
    # time.struct_time(tm_year=2013, tm_mon=10, tm_mday=10, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=3, tm_yday=283, tm_isdst=-1)
    # 2013
    # <class 'int'>