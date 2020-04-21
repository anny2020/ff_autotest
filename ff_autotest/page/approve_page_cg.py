# @Time: 2020/4/8  14:34
#撤管待审批页面及审批操作
from common.base import Base
from selenium import webdriver
import time

class Approve_cg():
    def __init__(self,driver):
        self.driver = driver
        self.base = Base(self.driver)
        #定位用户名元素的参数
        self.loc_user = ("id","txtUserName")
        #定位密码元素的参数
        self.loc_pwd = ("id","txtPassWord")
        #定位登录按钮元素的参数
        self.button = ("id","btnSubmit")
        #首页导航菜单中的“涉访管理”按钮元素
        self.loc_sfgl = ("css selector",".nav-feifang-n>a>cite>p")
        #涉访审批管理菜单元素
        self.loc_spgl = ("link text","涉访审批管理")
        #“撤管待审批”菜单元素
        self.loc_cgdsp = ("link text","撤管待审批")
        # 只能用JS来定位到“审批按钮”
        self.appr_butn = '''document.getElementsByTagName('iframe')[2].contentWindow.document.body.
        getElementsByClassName('layui-table-body')[1].getElementsByClassName('layui-btn')[0].click()'''
        #审批结果：选择同意或不同意，index为1是同意，为0是不同意
        self.appr_result = '''document.getElementsByTagName('iframe')[3].contentWindow.document.body.
        getElementsByTagName('fieldset')[1].getElementsByClassName('layui-anim')[1].click()'''
        #审批意见框
        self.appr_idea = '''document.getElementsByTagName('iframe')[3].contentWindow.document.
        body.getElementsByTagName('fieldset')[1].getElementsByClassName('layui-textarea')[0].value=("可以")'''
        #提交审批按钮
        self.appr_submit = '''document.getElementsByTagName('iframe')[3].contentWindow.document.
        getElementById("spButton").click()'''
        #审批“操作成功”提示
        self.submit_tips = ("css selector",".layui-layer-content.layui-layer-padding")

    #登录审批所长帐号、进入列管待审批列表
    def approve_list(self,username,password):
        self.base.send_key(self.loc_user,username)
        self.base.send_key(self.loc_pwd,password)
        self.base.click(self.button)
        self.base.click(self.loc_sfgl)
        self.base.click(self.loc_spgl)
        self.base.click(self.loc_cgdsp)
        time.sleep(2)
        self.driver.execute_script(self.appr_butn)
        time.sleep(2)
        self.driver.switch_to.default_content()

    def approve(self):
        # 执行JS脚本，选择审批结果为：同意
        self.driver.execute_script(self.appr_result)
        #录入审批意见
        self.driver.execute_script(self.appr_idea)
        #提交审批
        self.driver.execute_script(self.appr_submit)
        #提交审批后，页面返回到弹窗之外的页面
        self.driver.switch_to.default_content()

#所长在撤管待审批列表中提交审批，判断是否“操作成功”
    def is_submit_success(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    appr = Approve_cg(driver)
    appr.approve_list("01003","000000")
    appr.approve()
    result = appr.is_submit_success("操作成功")


