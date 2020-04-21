# @Time: 2020/4/8  10:58
from page.apply_manage_page import Apply_manage
from selenium import webdriver
from unittest import TestCase
import ddt
'''
用例设计：
使用01004警员帐号对已列管成功人员进行新增稳控操作
期望结果：新增成功
'''
data = [{"username":"01003","passwd":"000000","expect":"操作成功","location":"火车站西广场","wkdes":"稳控描述",
         "show":"表现正常","remark":"无"}]

@ddt.ddt
class Xzwk(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.add_sqlg = Apply_manage(cls.driver)


    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*data)
    def test_xzwk(self,data):
        print("---------------开始测试-----------------")
        print("测试数据是：%s %s %s %s %s %s %s" % (data["username"],data["passwd"],data["expect"],
                                              data["location"],data["wkdes"],data["show"],data["remark"]))
        self.add_sqlg.login(data['username'],data['passwd'])
        self.add_sqlg.xzwk(data["location"],data["wkdes"],data["show"],data["remark"])
        result = self.add_sqlg.is_submit_success(data['expect'])
        self.assertTrue(result)
        print("----------------结束测试------------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


