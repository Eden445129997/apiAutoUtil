import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi


class registerLogin(unittest.TestCase):
    """敲酷手机验证码登录"""
    #初始化
    def setUp(self):
        # 用户手机号
        self.userPhone = 15361899636
        self.smsCode = None
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def testLogin(self):

        userPhone = str(self.userPhone)
        smsCode = self.smsCode

        ykLoginParams = {
            "udid":"123",
        }
        # 游客登录
        response = LoginApi.ykLogin(ykLoginParams)

        userId = response.get("data").get("userId")
        accessToken = response.get("data").get("accessToken")

        # 如果没有验证码，则获取验证码到手机号
        if not smsCode:
            startCaptchaParams = {
                "userPhone":userPhone,
            }
            # 极验验证
            response = LoginApi.startCaptcha(startCaptchaParams)

            getSmsCodeParams = {
                    "userPhone":userPhone,
                    "udid":"123",
                }
            getSmsCodeParams["challenge"] = response.get("data").get("challenge")
            getSmsCodeParams["type"] = "1"
            # 获取短信验证码
            response = LoginApi.getSmsCode(getSmsCodeParams)

        # 如果有验证码，则登录，并且获取登录token
        if smsCode:
            smsCode = str(smsCode)
            checkSmsCodeData = {
                    "userPhone":userPhone,
                    "type":"1",
                }

            checkSmsCodeData["smsCode"] = str(smsCode)

            # 验证短信验证码——登录——将touken传入请求头
            response = LoginApi.checkSmsCode(checkSmsCodeData,accessToken)
            accessToken = response.get("data").get("accessToken")
            # return userId,accessToken
        # return userId,False

if __name__ == '__main__':
    unittest.main()

