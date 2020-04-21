# @Time: 2020/4/7  9:05
from page.approve_page import Approve
from page.apply_manage_page import Apply_manage
from selenium import webdriver
import time
from unittest import TestCase
import ddt
'''
用例设计：
所长01003对审批列表中“待审批”的列管人员进行审批操作，审批结论是：同意列管，提交审批成功
下一步为待局长审批
期望结果：所长审批成功
待优化：test_sslg_01和test_sslg_02可以合并为一个文件
'''
#列管审批所有的参数集
testdata=[{'username':'01004','passwd':'000000','sfzh':'412000123456789009','gkly':'公安部交办',
           'phone':'5678765','appr_user':'01003','appr_pawd':'000000','result':'操作成功'}]
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
        print("测试数据：%s %s %s %s %s %s %s %s" % (data["username"],data["passwd"],data["sfzh"]
        ,data["gkly"],data["phone"],data["appr_user"],data["appr_pawd"],data["result"]))
        self.add_sqlg.login(data["username"],data["passwd"])
        self.add_sqlg.sqlg(data["sfzh"],data["gkly"],data["phone"])
        self.tearDown()
        self.setUp()
        self.splg.approve_list(data["appr_user"],data["appr_pawd"])
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
