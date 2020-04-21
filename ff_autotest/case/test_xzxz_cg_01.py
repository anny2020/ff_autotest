# @Time: 2020/4/8  14:05
from page.apply_manage_page import Apply_manage
from selenium import webdriver
from unittest import TestCase
import ddt
'''
用例设计：
使用01004警员帐号对已列管成功人员进行新增撤管操作，操作成功后提交至01003所长处理
期望结果：新增提交成功
'''
data = [{"usrname":"01004","passwd":"000000","remark":"可以撤管","expect":"操作成功"}]
@ddt.ddt
class xzcg(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.add_sqlg = Apply_manage(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*data)
    def test_xzcg(self,data):
        print("------------------开始测试-----------")
        print("测试数据是：%s %s %s" % (data["usrname"],data["passwd"],data["remark"]))
        self.add_sqlg.login(data["usrname"],data["passwd"])
        self.add_sqlg.sqcg(data["remark"])
        result = self.add_sqlg.is_submit_success(data["expect"])
        print("------------------结束测试-------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()