# @Time: 2020/4/16  11:46
from page.apply_manage_page import Apply_manage
from selenium import webdriver
import time
from unittest import TestCase
import ddt
#打开涉访管理中的人员档案
'''
用例设计
涉访管理--->人员档案
期望结果：
成功打开人员档案
'''
#申请列管所有的参数集

class Apply_management(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.sqlg = Apply_manage(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    def test_sqlg(self):
        print("------------开始测试------------")
        self.sqlg.login("01003","000000")
        self.sqlg.mem_archive()
        result = self.sqlg.get_archive_title("人员档案")
        self.assertTrue(result)
        print("--------------测试结束----------------")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
