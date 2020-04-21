# @Time: 2020/4/16  9:54
from page.receive_notice_page import Receive_notice
from selenium import webdriver
from unittest import TestCase
import time
'''
接收通知模块-->用例设计:
1.局长帐号下发通知，所长帐号查看接收到的消息，签收操作；期望结果：签收成功
2.所长帐号针对接收到的通知，进行转发操作；期望结果：转发成功
'''
class Noti(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.notice = Receive_notice(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

# 局长下发通知，所长签收通知
    def test_trans_notice_01(self):
        print("----------开始测试01---------------")
        self.notice.login("01002","000000")
        self.notice.send("04161011","大河网1","内容1")
        time.sleep(2)
        self.notice.logout()
        self.notice.login("01003","000000")
        self.notice.receive_notice_sign()
        result = self.notice.get_notice_sign_tips("操作成功")
        self.assertTrue(result)
        print("----------结束测试01---------------")
#转发通知  此处目前服务连接异常
    # def test_trans_notice_02(self):
    #     print("----------开始测试02---------------")
    #     self.notice.login("01002","000000")
    #     #局长下发通知
    #     self.notice.send("test","test","test")
    #     self.notice.logout()
    #     # 所长签收通知
    #     self.notice.login("01003","000000")
    #     self.notice.receive_notice_sign()
    #     time.sleep(2)
    #     #所长签收完成后转发通知
    #     self.notice.transmit()
    #     result = self.notice.get_notice_trans_succ("操作成功")
    #     self.assertTrue(result)
    #     print("----------结束测试02---------------")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
