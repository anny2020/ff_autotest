# @Time: 2020/4/8  11:28
from page.apply_manage_page import Apply_manage
from selenium import webdriver
from unittest import TestCase
import ddt
'''
用例设计：
使用01004警员帐号对已列管成功人员进行打击处理操作
期望结果：新增成功
'''
data = [{"username":"01003","passwd":"000000","expect":"操作成功","hitreason":"去北京上访","remark":"无"}]

@ddt.ddt
class xzdacl(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.add_sqlg = Apply_manage(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")

    @ddt.data(*data)
    def test_djcl(self,data):
        print("---------------开始测试-----------------")
        print("测试数据是：%s %s %s" % (data['username'],data['passwd'],data['expect']))
        self.add_sqlg.login(data['username'],data['passwd'])
        self.add_sqlg.djcl(data["hitreason"],data['remark'])
        result = self.add_sqlg.is_submit_success(data['expect'])
        self.assertTrue(result)
        print("---------------结束测试------------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()