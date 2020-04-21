# @Time: 2020/4/10  11:35
from page.mgsqgl_page import Mgsqgl
from selenium import webdriver
from unittest import TestCase
import ddt
import time
'''
用例设计1：敏感时期管理-->添加敏感时期->关闭
期望结果：取消保存，未打开预警分值设置弹窗
用例设计2：敏感时期管理-->添加敏感时期->保存-->预警分值设置-->取消，不进入预警分值设置页面
期望结果：保存成功，打开预警分值弹窗，但未进入预警分值设置
用例设计3：敏感时期管理-->添加敏感时期->保存-->预警分值设置-->确定，进入预警分值设置页面
期望结果：保存成功，并进入预警分值设置页面
用例设计4：敏感时期管理-->添加敏感时期->保存-->预警分值设置-->确定，进入预警分值设置页面-->设置完成，提交
期望结果：预警分值设置成功
用例设计5：敏感时期管理--> 查看敏感时期
期望结果：打开查看页面
用例设计6：敏感时期管理-->编辑敏感时期
期望结果：打开编辑页面
用例设计7：敏感时期管理-->导入人员
期望结果：导入人员成功
用例设计8：敏感时期管理-->删除敏感时期
期望结果：删除成功
用例设计9：敏感时期管理-->查看报告
期望结果：打开查看报告页面
'''
class Mgsq_tj(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.mgsqgl = Mgsqgl(cls.driver)

    def setUp(self):
        self.driver.get("http://192.168.30.185:8082/ffyj/login.html")


#添加敏感时期后，点击“关闭”不保存
    def test_mgsq_tj_01(self):
        print("-------------开始测试01-------------")
        self.mgsqgl.login("01004","000000")
        self.mgsqgl.mgsqgl_list()
        self.mgsqgl.mgsqgl_close()
        result = self.mgsqgl.is_set_early_warn()
        self.assertFalse(result)
        print("-------------结束测试01--------------")

#是否预警分值设置：取消，不再打开预警分值页面
    def test_mgsq_tj_02(self):
        print("-------------开始测试02-------------")
        self.mgsqgl.login("01004","000000")
        self.mgsqgl.mgsqgl_list()
        self.mgsqgl.mgsqgl_save()
        self.mgsqgl.mgsqgl_qxyj()
        result = self.mgsqgl.is_open_early_warn()
        self.assertFalse(result)
        print("-------------结束测试02--------------")

#是否预警分值设置：确定，打开预警分值页面
    def test_mgsq_tj_03(self):
        print("-------------开始测试03-------------")
        self.mgsqgl.login("01004","000000")
        self.mgsqgl.mgsqgl_list()
        self.mgsqgl.mgsqgl_save()
        self.mgsqgl.mgsqgl_jryj()
        result = self.mgsqgl.is_open_early_warn()
        self.assertTrue(result)
        print("-------------结束测试03--------------")

#设置预警分值页面，提交
    def test_mgsq_tj_04(self):
        print("-------------开始测试04-------------")
        self.mgsqgl.login("01004","000000")
        self.mgsqgl.mgsqgl_list()
        self.mgsqgl.mgsqgl_save()
        self.mgsqgl.mgsqgl_jryj()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.mgsqgl.szyjz("45")
        #此处无法做判断了，因为提交后没有提交成功提示
        print("-------------结束测试04--------------")

        #敏感时期管理列表页：查看敏感时期
    def test_mgsq_tj_05(self):
        print("-------------开始测试05-------------")
        self.mgsqgl.login("01004","000000")
        self.mgsqgl.click_view()
        result = self.mgsqgl.get_title("查看")
        self.assertTrue(result)
        print("-------------结束测试05--------------")
        #敏感时期管理列表页：编辑敏感时期
    def test_mgsq_tj_06(self):
        print("-------------开始测试06-------------")
        self.mgsqgl.login("01004","000000")
        self.mgsqgl.click_edit()
        result = self.mgsqgl.get_submit_text("提交")
        self.assertTrue(result)
        print("-------------结束测试06--------------")

    #敏感时期管理列表页：导入人员
    # def test_mgsq_tj_07(self):
    #     print("-------------开始测试07-------------")
    #     self.mgsqgl.login("01003","000000")
    #     self.mgsqgl.import_mem()
    #     result = self.mgsqgl.get_import_result("导入结果")
    #     self.assertTrue(result)
    #     print("-------------结束测试07--------------")

    #删除敏感时期
    def test_mgsq_del_08(self):
        print("-------------开始测试08-------------")
        self.mgsqgl.login("01003","000000")
        self.mgsqgl.delete()
        result = self.mgsqgl.del_success("删除成功")
        self.assertTrue(result)
        print("-------------结束测试08--------------")

     #删除敏感时期
    def test_mgsq_del_09(self):
        print("-------------开始测试09-------------")
        self.mgsqgl.login("01003","000000")
        self.mgsqgl.view_report()
        result = self.mgsqgl.get_title("查看报告")
        self.assertTrue(result)
        print("-------------结束测试09--------------")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver .quit()