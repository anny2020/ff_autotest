# @Time: 2020/4/1  13:28
'''
用例设计：
登录用例1：用户名、密码录入正确
期望结果：登录成功
登录用例2：用户名、密码错误
期望结果：登录失败
'''
from unittest import TestCase
import time
from selenium import webdriver
from page.login_page import LoginPage
import ddt
#登录所有的参数集
testdata = [{'username':'00000','passwd':'000000','expect':'省厅管理员'},
            {'username':'0000','passwd':'00000','expect':''}]

@ddt.ddt
class TestLogin(TestCase):

    @classmethod
#执行所有用例之前的初始化工作
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_page = LoginPage(cls.driver)

#执行单条用例之前的初始化工作
    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

#登录成功的方法
    def login(self,username,passwd,expect):
        self.login_page.input_username(username)
        self.login_page.input_pwd(passwd)
        self.login_page.click_submit()
        username = self.login_page.get_login_username()
        self.assertTrue(username == expect)

    @ddt.data(*testdata)
    def test_case_01(self,data):
        print("-------------开始测试------------------")
        print("测试数据为：%s %s %s" % (data["username"],data["passwd"],data["expect"]))
        self.login(data["username"],data["passwd"],data["expect"])
        print("---------------结束测试------------------")

#单条用例执行完检查是有alert、清cookies、刷新
    def tearDown(self):
#单条用例执行完后判断下是否有alert弹窗，如果有的话关闭弹窗，避免影响下条用例的正常执行
        self.login_page.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

#用例全部执行完退出浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

