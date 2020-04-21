# @Time: 2020/4/14  10:39
from page.send_notice_page import Add_notice
from selenium import webdriver
from unittest import TestCase
'''
下发通知模块-->用例设计:
1.所长帐号进行下发通知操作；期望结果：新增下发通知成功
2.所长帐号点击查看通知详情；期望结果：打开通知公告详情
3.所长帐号点击查看签收情况；期望结果：打开签收情况
'''
class Noti(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.notice = Add_notice(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")
# 新增下发通知
    def test_notice_01(self):
        print("----------开始测试01---------------")
        self.notice.login("01002","000000")
        self.notice.add_notice("最新0421","宜昌公安网","近日，市委宣传部、市公安局发布宜昌市疫情防控"
                                              "通报，向郑承瑛等50名奋战在疫情防控一线的公安干警致敬！")
        result = self.notice.add_notice_tips("操作成功")
        self.assertTrue(result)
        print("----------结束测试01---------------")

#查看通知详情
    def test_send_notice_02(self):
        print("----------开始测试02---------------")
        self.notice.login("01002","000000")
        self.notice.notice_detail()
        result = self.notice.get_notice_detail_title("通知公告详情")
        self.assertTrue(result)
        print("----------结束测试02---------------")
#查看签收情况
    def test_send_notice_03(self):
        print("----------开始测试03---------------")
        self.notice.login("01002","000000")
        self.notice.recei_detail()
        result = self.notice.get_notice_detail_title("签收情况")
        self.assertTrue(result)
        print("----------结束测试03---------------")


    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


