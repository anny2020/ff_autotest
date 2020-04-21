# @Time: 2020/4/9  14:08
# @Time: 2020/4/9  11:44
from page.sfqtgl_page import Sfqt
from selenium import webdriver
from unittest import TestCase
import ddt
'''用例设计：
添加活动记录
期望结果：添加成功
'''
data = [{"username":"01004","passwd":"000000","expect":"操作成功"}]

@ddt.ddt
class sfqt(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.sfqt = Sfqt(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*data)
    def test_hdjl(self,data):
        print("--------------开始测试------------------")
        print("测试数据是：%s %s" % (data['username'],data['passwd']))
        self.sfqt.login(data['username'],data['passwd'])
        self.sfqt.del_qt()
        result = self.sfqt.is_submit_success(data["expect"])
        print("---------------测试结束-------------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

