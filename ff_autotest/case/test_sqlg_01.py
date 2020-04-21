# @Time: 2020/4/2  11:30
from page.apply_manage_page import Apply_manage
from selenium import webdriver
import time
from unittest import TestCase
import ddt
#申请列管
'''
用例设计-正常流程：申请列管提交审批
涉访管理--->申请列管--->录入列管人员身份证号码为存在人员且未列管：查询后带出人员基本信息,补充录入列管信息必填项（管控来源、
管控等级、涉访诉求、稳控状态、当前状态、联系电话），提交列管，提交成功
期望结果：
进入待审批列表
'''
#申请列管所有的参数集
testdata=[{'username':'01004','passwd':'000000','sfzh':'411000123456781008','gkly':'公安部交办',
           'phone':'5678765','tips':'操作成功'}]

@ddt.ddt
class Apply_management(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.add_sqlg = Apply_manage(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*testdata)
    def test_sqlg(self,data):
        print("------------开始测试------------")
        print("测试数据为%s %s %s %s %s %s" % (data["username"],data["passwd"],data["sfzh"],
                                       data["gkly"],data["phone"],data["tips"]))
        self.add_sqlg.login(data["username"],data["passwd"])
        self.add_sqlg.sqlg(data["sfzh"],data["gkly"],data["phone"])
        result = self.add_sqlg.is_submit_success(data["tips"])
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
