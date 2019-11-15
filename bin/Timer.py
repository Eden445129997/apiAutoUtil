import os
import time
from apiAutoUtil.config.path import binPath
from apiAutoUtil.src.utils.Log import log

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
    start = timer()
    start.timerExecute()