# @Time: 2020/4/2  17:22
#列管待审批页面及审批操作
from common.base import Base
from selenium import webdriver
import time

class Approve():
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
        #涉访审批管理菜单元素
        self.loc_spgl = ("link text","涉访审批管理")
        #“列管待审批”菜单元素
        self.loc_lgdsp = ("link text","列管待审批")
        #定位待审批的表格 未用到
        self.loc_table = ("css selector","#fsDatagrid")
        #定位表格内容td  未用到
        self.loc_table_td = ("tag name","td")
        #定位审批按钮
        # 只能用JS来定位到“审批按钮”
        self.appr_butn = '''document.getElementsByTagName('iframe')[2].contentWindow.document.body.
        getElementsByClassName('layui-table-body')[1].getElementsByClassName('layui-btn')[0].click()'''
        #-----------------审批弹窗页--------------------
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
        self.base.click(self.loc_lgdsp)
        time.sleep(2)
        self.driver.execute_script(self.appr_butn)
        self.driver.switch_to.default_content()

    def approve(self):
        #执行JS脚本，选择审批结果为：同意
        self.driver.execute_script(self.appr_result)
        #录入审批意见
        self.driver.execute_script(self.appr_idea)
        #提交审批
        self.driver.execute_script(self.appr_submit)
        #提交审批后，页面返回到弹窗之外的页面
        self.driver.switch_to.default_content()
#所长在列管待审批列表中提交审批，判断是否“操作成功”
    def is_submit_success(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result


#审批前确先获取到列表中第一行人员身份证号，用于判断是不是上一流程提交的待审批人员，未用，先注掉
    # def get_appr_list_user(self):
    #     #获取表格对象
    #     ele = self.base.findElement(self.loc_table)
    #     #提取表格内容       这个地方有点慢，需要再优化！！！！！！！！！！！！！！
    #     td_content = self.base.findElements(self.loc_table_td)
    #     list = []
    #     for td in td_content:
    #         list.append(td.text)
    #     #把第一行的身份证号值返回
    #     return list[3]

#判断待审批的人员是不是上一流程添加的人员，这个判断暂时不加了,因为判断这个时间和JS中的切换iframe有冲突了
    # def is_right_person(self,person):
    #     #拿到第一行人员身份证号，和上一流程提交的待审批人员身份证号进行比较
    #     get_list_user = self.get_appr_list_user()
    #     if (get_list_user == person):
    #         return True
    #     else:
    #         return False

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    appr = Approve(driver)
    appr.approve_list("01003","000000")
    time.sleep(2)
    appr.approve()







