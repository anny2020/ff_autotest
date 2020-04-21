# @Time: 2020/4/8  15:52
#涉访群体管理页面
from common.base import Base
from selenium import webdriver
import time

class Sfqt():
#初始化涉访群体管理页面的元素参数
    def __init__(self,driver):
        self.driver = driver
        self.base = Base(driver)
        #定位用户名元素的参数
        self.loc_user = ("id","txtUserName")
        #定位密码元素的参数
        self.loc_pwd = ("id","txtPassWord")
        #定位登录按钮元素的参数
        self.button = ("id","btnSubmit")
        #首页导航菜单中的“涉访管理”按钮元素
        self.loc_sfgl = ("css selector",".nav-feifang-n>a>cite>p")
        #涉访群体管理菜单
        # self.loc_sfqtgl = ("text link","涉访群体管理")
        self.loc_sfqtgl = ("xpath",".//*[@id='fsLeftMenu']/li[4]/a")
        #新增群体按钮
        self.loc_xzqt = ("xpath","html/body/div/div/div/div[2]/div/div[1]/button")
        #新增群体弹窗：群体名称   /和编辑页面共用名称
        self.loc_xzqt_mc = ("name","mc")
        #新增群体弹窗：所在地市
        self.loc_xzqt_szds = ("name","szds")
        #新增群体弹窗：群体人数
        self.loc_xzqt_qtrs = ("name","qtrs")
        #新增群体弹窗：群体诉求
        self.loc_xzqt_qtsq = ("name","qtsq")
        #新增群体弹窗：新增按钮
        self.loc_xzqt_add = ("xpath","html/body/div/form/div[6]/button[1]")
        #"提交成功提示"
        self.loc_submit_tip = ("css selector",".layui-layer-content.layui-layer-padding")
        #--------------编辑群体按钮
        self.loc_edit_qtsj = '''document.getElementsByTagName('iframe')[2].contentWindow.document.body.
                                getElementsByTagName('tbody')[1].getElementsByTagName('a')[1].click()'''
        #编辑群体事件：提交按钮
        self.loc_edit_submit = ("xpath","html/body/div[1]/form/div[5]/button[1]")
        #-------------添加活动记录按钮
        self.loc_add_hdjl = '''document.getElementsByTagName('iframe')[2].contentWindow.
        document.body.getElementsByTagName('tbody')[1].getElementsByTagName('a')[2].click()'''
        #添加活动记录：活动时间
        self.loc_hdsj = ("id","test5")
        #添加活动记录：选择时间确定按钮
        self.loc_data_confirm = ("css selector",".laydate-btns-confirm")
        #添加活动记录：活动内容
        self.loc_content = ("name","content")
        #添加活动记录：提交按钮
        self.loc_submit = ("xpath","html/body/div/form/div[3]/button")
        #----------删除涉访群体-------------
        self.loc_del_qt = '''document.getElementsByTagName('iframe')[2].contentWindow.document.body.
                                getElementsByTagName('tbody')[1].getElementsByTagName('a')[3].click()'''
        #删除涉访群体：确定删除按钮
        self.loc_del_confirm = ("css selector",".layui-layer-btn0")

#登录帐号
    def login(self,username,passwd):
        self.base.send_key(self.loc_user,username)
        self.base.send_key(self.loc_pwd,passwd)
        self.base.click(self.button)
#新增群体
    def xzqt(self,mc,szds,qtrs,qtsq):
        self.base.click(self.loc_sfgl)
        time.sleep(2)
        self.base.click(self.loc_sfqtgl)
        self.driver.switch_to.frame(2)
        time.sleep(2)
        self.base.click(self.loc_xzqt)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame("layui-layer-iframe2")
        self.base.send_key(self.loc_xzqt_mc,mc)
        self.base.send_key(self.loc_xzqt_szds,szds)
        self.base.send_key(self.loc_xzqt_qtrs,qtrs)
        self.base.send_key(self.loc_xzqt_qtsq,qtsq)
        self.base.click(self.loc_xzqt_add)
        self.driver.switch_to.default_content()

#编辑群体
    def bjqt(self,mc,szds,qtrs,qtsq):
        self.base.click(self.loc_sfgl)
        time.sleep(2)
        self.base.click(self.loc_sfqtgl)
        time.sleep(3)
        self.driver.execute_script(self.loc_edit_qtsj)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(3)
        self.base.clear(self.loc_xzqt_mc)
        self.base.send_key(self.loc_xzqt_mc,mc)
        self.base.clear(self.loc_xzqt_szds)
        self.base.send_key(self.loc_xzqt_szds,szds)
        self.base.clear(self.loc_xzqt_qtrs)
        self.base.send_key(self.loc_xzqt_qtrs,qtrs)
        self.base.clear(self.loc_xzqt_qtsq)
        self.base.send_key(self.loc_xzqt_qtsq,qtsq)
        time.sleep(2)
        self.base.click(self.loc_edit_submit)
        self.driver.switch_to.default_content()

#添加活动记录
    def add_hdjl(self,hdnr):
        self.base.click(self.loc_sfgl)
        time.sleep(2)
        self.base.click(self.loc_sfqtgl)
        time.sleep(3)
        self.driver.execute_script(self.loc_add_hdjl)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(3)
        self.base.click(self.loc_hdsj)
        self.base.click(self.loc_data_confirm)
        self.base.send_key(self.loc_content,hdnr)
        self.base.click(self.loc_submit)
        self.driver.switch_to.default_content()

#删除群体
    def del_qt(self):
        self.base.click(self.loc_sfgl)
        time.sleep(2)
        self.base.click(self.loc_sfqtgl)
        time.sleep(3)
        self.driver.execute_script(self.loc_del_qt)
        self.driver.switch_to.frame(2)
        self.base.click(self.loc_del_confirm)



    def is_submit_success(self,text):
         result = self.base.is_text_in_element(self.loc_submit_tip,text)
         return result

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    sfqt = Sfqt(driver)
    sfqt.login("01004","000000")
    sfqt.del_qt()

