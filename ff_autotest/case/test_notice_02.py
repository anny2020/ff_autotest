# @Time: 2020/4/14  16:14
from page.receive_notice_page import Receive_notice
from selenium import webdriver
from unittest import TestCase
'''
接收通知模块-->用例设计:
1.警员帐号点击接收通知列表第一条通知详情；期望结果：打开通知公告详情
2.警员进行签收操作；期望结果：签收成功
'''
class Noti(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.notice = Receive_notice(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")
#新增下发通知,打开通知公告详情
    def test_recei_notice_01(self):
        print("----------开始测试01---------------")
        self.notice.login("01002","000000")
        self.notice.send("2020042002","新浪","内容")
        self.notice.logout()
        self.notice.login("01003","000000")
        self.notice.receive_notice_detail()
        result = self.notice.get_notice_detail_title("通知公告详情")
        self.assertTrue(result)
        print("----------结束测试01---------------")

#签收
    def test_recei_notice_02(self):
        print("----------开始测试02---------------")
        self.notice.login("01003","000000")
        self.notice.receive_notice_sign()
        result = self.notice.get_notice_sign_tips("操作成功")
        self.assertTrue(result)
        print("----------结束测试02---------------")


    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


