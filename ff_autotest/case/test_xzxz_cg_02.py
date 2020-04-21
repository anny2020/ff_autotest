# @Time: 2020/4/8  14:31
from page.approve_page_cg import Approve_cg
from selenium import webdriver
from unittest import TestCase
import ddt
'''用例设计：
1:使用01003所长帐号对撤管待审批人员进行审批，结果为同意，审批成功
期望结果：所长审批成功
2:使用01002局长帐号对撤管待审批人员进行审批，结果为同意，审批成功，撤管完成
期望结果：局长审批成功
'''
data = [{"username":"01003","passwd":"000000","expect":"操作成功"},
        {"username":"01002","passwd":"000000","expect":"操作成功"}]

@ddt.ddt
class sqcg_sp(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.appr_cg = Approve_cg(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*data)
    def test_appr_cg(self,data):
        print("----------------开始测试------------------")
        print("测试数据是：%s %s %s" % (data["username"],data["passwd"],data["expect"]))
        self.appr_cg.approve_list(data["username"],data["passwd"])
        self.appr_cg.approve()
        result = self.appr_cg.is_submit_success(data["expect"])
        self.assertTrue(result)
        print("---------------结束测试--------------------")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()