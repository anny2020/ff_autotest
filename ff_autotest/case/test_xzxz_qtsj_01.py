# @Time: 2020/4/8  16:54
from page.sfqtgl_page import Sfqt
from selenium import webdriver
from unittest import TestCase
import ddt
'''用例设计：
新增群体事件
期望结果：新增成功
'''
data = [{"username":"01004","passwd":"000000","mc":"讨薪0409",
         "szds":"郑州","qtrs":"50","qtsq":"工资","expect":"操作成功"}]

@ddt.ddt
class sfqt(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.sfqt = Sfqt(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*data)
    def test_add_qtsj(self,data):
        print("---------------开始测试---------------")
        print("测试数据：%s %s %s %s %s %s %s" % (data["username"],data["passwd"],data["mc"],
            data["szds"],data["qtrs"],data["qtsq"],data["expect"]))
        self.sfqt.login(data["username"],data["passwd"])
        self.sfqt.xzqt(data["mc"],data["szds"],data["qtrs"],data["qtsq"])
        result = self.sfqt.is_submit_success(data["expect"])
        self.assertTrue(result)
        print("--------------结束测试-----------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

