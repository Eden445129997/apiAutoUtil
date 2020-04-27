import unittest
import time
import re

from config.gloVar import globalRides
from src.testCase.qiaoku import api_obj
from src.script.敲酷业务脚本 import getPhoneNum
from ddt import ddt,data,unpack

#第一个测试用例入参
phone_list = [getPhoneNum()]


@ddt
class registerLogin(unittest.TestCase):
    """注册登录模块"""
    #初始化
    def setUp(self):
        pass

    def tearDown(self):
        # 清理自动化的测试数据
        pass

    @data(*phone_list)
    def testa(self,phone):
        """获取手机验证码"""
        self.login(phone)
        smsCode = self.getSmsCode(phone)
        if smsCode:
            self.assertTrue(smsCode)

    @data(*phone_list)
    def testb(self,phone):
        """获取手机验证码方式登录
            条件：正确的验证码
            预期：登录成功
        """
        self.autoLogin(phone)

    @data(*phone_list)
    def testc(self,phone):
        """获取手机验证码方式登录
            条件：错误的验证码
            预期：登录失败
        """
        self.login(phone)
        smsCode = self.getSmsCode(phone)
        # 错误的验证码登录
        if smsCode != 0000:
            self.login(phone,0000)
        else:
            pass

    def login(self,userPhone,smsCode=None,udid="tester_eden",type="1"):
        """获取手机号码一键登录"""
        userPhone = str(userPhone)
        smsCode = smsCode

        ykLoginParams = {
            "udid": udid,
        }
        # 游客登录
        response = api_obj.login_ykLogin(ykLoginParams)

        self.assertEqual(response.get("code"),200,"游客登录状态码异常")

        try:
            userId = response.get("data").get("userId")
            accessToken = response.get("data").get("accessToken")
        except:
            return False,False

        # 如果没有验证码，则获取验证码到手机号
        if not smsCode:
            startCaptchaParams = {
                "userPhone":userPhone,
            }
            # 极验验证
            response = api_obj.login_startCaptcha(startCaptchaParams)
            self.assertEqual(response.get("code"),200,"极验验证状态码异常")


            getSmsCodeParams = {
                    "userPhone":userPhone,
                    "udid": udid,
                }

            getSmsCodeParams["challenge"] = response.get("data").get("challenge")
            getSmsCodeParams["type"] = "1"
            # 获取短信验证码
            response = api_obj.login_getSmsCode(getSmsCodeParams)
            self.assertEqual(response.get("code"),200,"获取短信验证码状态码异常")

        # 如果有验证码，则登录，并且获取登录token
        if smsCode:
            smsCode = str(smsCode)
            checkSmsCodeData = {
                    "userPhone":userPhone,
                    "type":type,
                    "udid": udid,
                }

            checkSmsCodeData["smsCode"] = str(smsCode)

            # 验证短信验证码——登录——将touken传入请求头
            response = api_obj.login_checkSmsCode(checkSmsCodeData,accessToken)
            if smsCode != 0000:
                self.assertEqual(response.get("code"),200,"验证短信验证码状态码异常")
                accessToken = response.get("data").get("accessToken")
            else:
                self.assertEqual(response.get("code"),400,"验证短信验证码状态码异常")
            return userId,accessToken
        return userId,False

    def autoLogin(self,phoneNum):
        """自动登录获取userId，token"""

        # 发送验证码
        self.login(phoneNum)
        time.sleep(1)

        # 获取redis的smsCode
        smsCode = self.getSmsCode(phoneNum)
        # print(smsCode)
        if smsCode:
            # 处理redis获取的数据提取验证码
            smsCode = re.findall(r'\d+',smsCode)
            # print(smsCode)
            smsCode = smsCode[0]

            # 登录获取token
            userId,token = self.login(phoneNum,smsCode)

            return userId,token
        return False,False

    def getSmsCode(self,phone):
        """redis获取验证码"""
        rds,__ = globalRides()
        token = rds.get("smsCode:%s,app"%phone)
        # 获取token
        return str(token)

if __name__ == '__main__':
    unittest.main()

