# @Time: 2020/4/7  11:43
# @Time: 2020/4/7  9:05
from page.approve_page import Approve
from page.apply_manage_page import Apply_manage
from selenium import webdriver
import time
from unittest import TestCase
import ddt
'''
用例设计：
局长01002对审批列表中“待审批”的列管人员进行审批操作，审批结论是：同意列管，提交审批成功
期望结果：
局长审批成功
'''
#列管审批所有的参数集
testdata=[{'username':'01004','passwd':'000000','sfzh':'410225199002034137','gkly':'公安部交办',
           'phone':'5678765','appr1_user':'01003','appr1_pawd':'000000',
           'appr2_user':'01002','appr2_pawd':'000000','result':'操作成功'}]
@ddt.ddt
class splg(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.add_sqlg = Apply_manage(cls.driver)
        cls.splg = Approve(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*testdata)
    def test_splg(self,data):
        print("------------------开始测试--------------------")
        print("测试数据：%s %s %s %s %s %s %s %s %s %s" % (data["username"],data["passwd"],data["sfzh"],data["gkly"],
        data["phone"],data["appr1_user"],data["appr1_pawd"],data["appr2_user"],data["appr2_pawd"],data["result"]))
        self.add_sqlg.login(data["username"],data["passwd"])
        self.add_sqlg.sqlg(data["sfzh"],data["gkly"],data["phone"])
        self.tearDown()
        self.setUp()
        self.splg.approve_list(data["appr1_user"],data["appr1_pawd"])
        time.sleep(2)
        self.splg.approve()
        self.tearDown()
        self.setUp()
        self.splg.approve_list(data["appr2_user"],data["appr2_pawd"])
        time.sleep(2)
        self.splg.approve()
        result = self.splg.is_submit_success(data["result"])
        self.assertTrue(result)
        print("-----------------测试结束--------------------")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
