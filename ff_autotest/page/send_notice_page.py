# @Time: 2020/4/13  15:54
from common.base import Base
from selenium import webdriver
import time
#下发通知管理页面
class Add_notice():
    def __init__(self,driver):
        self.driver = driver
        self.base = Base(self.driver)
        #定位用户名元素的参数
        self.loc_user = ("id","txtUserName")
        #定位密码元素的参数
        self.loc_pwd = ("id","txtPassWord")
        #定位登录按钮元素的参数
        self.button = ("id","btnSubmit")
        #首页导航栏右箭头
        self.nav_left = ("css selector","#nav_left>img")
        #定位导航菜单通知公告
        self.menu_notice = ("css selector",".nav-tongzhi-n>a>cite>p")
        #下发通知按钮
        self.loc_add_notice = ("xpath","html/body/div/div/div/div[2]/div/div[1]/button")
        #------------下发通知弹窗-----------------
        #标题
        self.loc_headline = ("name","title")
        #来源
        self.loc_source = ("name","noticeSource")
        #内容
        self.loc_content = ("name","content")
        #附件 请求接口目前异常，此步暂时跳过
        self.loc_attach = ("name","fjIds")
        #点击选择单位
        self.loc_recei_depart = ("id","dwLookupBtn")
        #选择单位弹窗中的复选框
        self.loc_tree_check  = ("id","treeDemo_2_check")
        #选择按钮
        self.loc_sele = ("id","selectBtn")
        #通知标签
        self.loc_lable = ("xpath","html/body/div/form/div[6]/div/div[1]/span")
        #新增按钮
        self.loc_add = ("xpath","html/body/div[1]/form/div[7]/button[1]")
        #新增提交后提示信息
        self.submit_tips = ("css selector",".layui-layer-content.layui-layer-padding")
        #-----通知详情按钮
        self.notice_det = '''document.getElementsByTagName('iframe')[1].contentWindow.document.body.
        getElementsByTagName('a')[0].click()'''
        #-----通知详情弹窗title
        self.loc_title = ('css selector',".layui-layer-title")
        #--签收情况按钮
        self.notice_recei = '''document.getElementsByTagName('iframe')[1].contentWindow.document.body.
        getElementsByTagName('a')[1].click() '''




    #登录帐号
    def login(self,username,passwd):
        self.base.send_key(self.loc_user,username)
        self.base.send_key(self.loc_pwd,passwd)
        self.base.click(self.button)

#进入通知管理列表页,“下发通知”
    def add_notice(self,headline,source,content):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        self.driver.switch_to.frame(1)
        self.base.click(self.loc_add_notice)
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(2)
        self.base.send_key(self.loc_headline,headline)
        self.base.send_key(self.loc_source,source)
        self.base.send_key(self.loc_content,content)
        #请求接口目前异常，此步暂时跳过
        # self.base.send_key(self.loc_attach,r"C:\Users\Ling\Downloads\lksfmb.xlsx")
        self.base.click(self.loc_recei_depart)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(3)
        self.base.click(self.loc_tree_check)
        self.base.click(self.loc_sele)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(2)
        time.sleep(2)
        self.base.click(self.loc_lable)
        self.base.click(self.loc_add)
        self.driver.switch_to.default_content()

    #查看通知详情
    def notice_detail(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        time.sleep(1)
        self.driver.execute_script(self.notice_det)
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)

    #查看签收情况
    def recei_detail(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        time.sleep(1)
        self.driver.execute_script(self.notice_recei)
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)


    #获取下发通知提交后的提示信息
    def add_notice_tips(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result

    #获取通知公告详情弹窗的title
    def get_notice_detail_title(self,text):
        result = self.base.is_text_in_element(self.loc_title,text)
        return result

    #获取通知公告详情弹窗的title
    def get_notice_detail_title(self,text):
        result = self.base.is_text_in_element(self.loc_title,text)
        return result

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    notice = Add_notice(driver)
    notice.login("01002","000000")
    notice.add_notice("6","2","3")