# coding:utf-8
import unittest
import time
from apiAutoUtil.src.utils import HTMLTestRunner
from apiAutoUtil.config import path

import smtplib    #邮件发送的核心类
from email.mime.text import MIMEText  #初始化邮件内容
from email.header import Header   #初始化邮件头部信息
from email.mime.multipart import MIMEMultipart  #附件

class excuteTask():
    def __init__(self):
        self.now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())

        self.mail_host = 'smtp.163.com'
        self.mail_user = "Eden445129997@163.com"
        self.mail_password = "hongwenhui0105"

    def send_email(self,to_user,report):           #读取报告文件作为邮件内容
            '''
            发送邮件内容
            :param to_user:发送邮件的人
            :param sub:主题
            :param content:邮件内容
            '''
            # report = "auto_test.html"
            with open(report,"rb") as f:  #打开指定文件，以二进制的方式打开
                mail_content = f.read()
            # text_msg = MIMEText(mail_content,"plain","utf-8")
            text_msg = MIMEText(mail_content,"html","utf-8")  #配置邮件内容
            text_msg["Content_Type"] = "application/octet-stream" #配置邮件类型，默认写法
            text_msg["Content-Dispostion"] = '自动化测试报告'
            #创建一个带附件的邮件实例,作为根容器
            main_msg = MIMEMultipart()
            #将邮件显示内容添加到根容器
            main_msg.attach(text_msg)
            main_msg["From"] = self.mail_user      #配置邮件发送方
            main_msg["To"] = to_user            #配置邮件接收方
            # main_msg.attach(MIMEText(mail_content,"html","utf-8"))
            subject = "自动化测试报告"  #配置邮件主题
            main_msg["Subject"] = Header(subject,"utf-8")
            try:
                smtpobj = smtplib.SMTP_SSL(self.mail_host,465)  #配置发送端口及邮件服务
                smtpobj.login(self.mail_user,self.mail_password)  #配置邮箱登录名及授权码
                smtpobj.sendmail(self.mail_user,to_user,main_msg.as_string())  #配置邮件内容
                smtpobj.quit()
                print("邮件发送成功")
            except smtplib.SMTPException as fals_msg:
                print("发送邮件失败")
                print("失败信息%s"%fals_msg)

    #用例名,报告文件名,报告标题,测试者
    def buildTask(self,caseName="*",reportName="TestReport_",reportTitle="自动化测试报告",tester="Eden"):
        # html文件
        html = path.reportPath() + reportName + self.now + ".html"

        # 创建将报告写入的文件对象
        fp = open(html,"wb")

        # 生成报告的数据流向,报告头,测试者
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=reportTitle,tester=tester)

        # 批量导入测试用例进测试套件中
        suit = unittest.defaultTestLoader.discover(path.testCasePath() + "\\main",caseName + ".py")

        # 执行套件生成报告
        runner.run(suit)
        #关闭文件
        fp.flush()
        fp.close()

        self.send_email('445129997@qq.com',html)

if __name__ == '__main__':
    excute = excuteTask()
    excute.buildTask()