# @Time: 2020/4/14  14:31
from common.base import Base
from selenium import webdriver
# from page.send_notice_page import Add_notice
import time
import datetime
#接收通知管理页面
class Receive_notice():
    def __init__(self,driver):
        self.driver = driver
        self.base = Base(self.driver)
        # self.add_noti = Add_notice(self.driver)
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
        #定位接收通知管理菜单
        self.menu_receive_notice = ("link text","接收通知管理")
        #----接收通知列表---
        #获取列表中第一条通知的标题 暂未用 该元素定位可能不正确
        self.loc_list_title1 = '''("css selector",".layui-form.layui-border-box.layui-table-view>
        div[1]>div[2]>table>tbody>tr[1]>td[2]")'''
        #详情按钮
        self.loc_noti_detail = '''document.getElementsByTagName('iframe')[1].contentWindow.document.body.
        getElementsByTagName("a")[0].click()'''
        #详情弹窗title
        self.loc_title = ("css selector",".layui-layer-title")
        #签收按钮   / 签收完成后，转发按钮操作可复用此
        self.loc_notice_sign = '''document.getElementsByTagName('iframe')[2].contentWindow.document.body.
        getElementsByTagName("a")[1].click()'''
        #签收提示框，确定按钮
        self.loc_sign_confirm = ("css selector",".layui-layer-btn0")
        #签收操作成功提示
        self.submit_tips = ("css selector",".layui-layer-content.layui-layer-padding")
        #下发通知管理页面，为了完成签收操作前的准备，先执行下发通知-----------------
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

        #---------------登录用户登出--
        self.username = ("id","userName")
        self.exit = ("link text","退出")
        #------------------转发操作
        #选择单位弹窗中的复选框
        self.loc_tree_check  = ("id","treeDemo_2_check")
        #选择按钮
        self.loc_sele = ("id","selectBtn")
        # 转发按钮
        self.loc_trans = ("xpath",".//*[@id='myform']/div[8]/button[1]")

         #登录帐号
    def login(self,username,passwd):
        self.base.send_key(self.loc_user,username)
        self.base.send_key(self.loc_pwd,passwd)
        self.base.click(self.button)


#签收前先下发通知
    def send(self,title,source,content):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        self.driver.switch_to.frame(1)
        self.base.click(self.loc_add_notice)
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(4)
        self.driver.switch_to.frame(2)
        self.base.send_key(self.loc_headline,title)
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

#进入接收通知管理列表页,操作“详情”
    def receive_notice_detail(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        time.sleep(2)
        self.base.click(self.menu_receive_notice)
        self.driver.execute_script(self.loc_noti_detail)
        self.driver.switch_to.default_content()


#进入接收通知管理列表页,操作“签收”
    def receive_notice_sign(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        time.sleep(2)
        self.base.click(self.menu_receive_notice)
        time.sleep(2)
        self.driver.execute_script(self.loc_notice_sign)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(2)
        time.sleep(2)
        self.base.click(self.loc_sign_confirm)
        self.driver.switch_to.default_content()

# #操作查看签收情况
#     def signed_detail(self):
#         self.base.click(self.nav_left)
#         time.sleep(2)
#         self.base.click(self.menu_notice)
#         time.sleep(2)
#         self.base.click(self.menu_receive_notice)
#         time.sleep(2)
#         self.driver.execute_script(self.loc_noti_sign)
#         self.driver.switch_to.default_content()

# #获取签收情况title
#     def get_sign_detail_title(self,text):
#         result = self.base.is_text_in_element(self.loc_title,text)
#         return result

    #判断接收列表中的第一条数据标题是否和下发的标题一致 暂未用
    def get_list_title1(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        time.sleep(2)
        self.base.click(self.menu_receive_notice)
        time.sleep(2)
        self.driver.switch_to.frame(1)
        result = self.base.is_text_in_element(self.loc_list_title1,"04161009")
        return result

    #获取通知公告详情弹窗的title
    def get_notice_detail_title(self,text):
        result = self.base.is_text_in_element(self.loc_title,text)
        return result

    #获取签收成功提示
    def get_notice_sign_tips(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result

    #退出登录
    def logout(self):
        self.base.click(self.username)
        self.base.click(self.exit)
        time.sleep(2)

    #转发操作
    def transmit(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_notice)
        time.sleep(3)
        self.base.click(self.menu_receive_notice)
        time.sleep(2)
        self.driver.execute_script(self.loc_notice_sign)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(3)
        self.base.click(self.loc_recei_depart)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(4)
        self.base.click(self.loc_tree_check)
        self.base.click(self.loc_sele)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(3)
        time.sleep(2)
        self.base.click(self.loc_trans)
        self.driver.switch_to.default_content()
   #判断是否转发操作成功
    def get_notice_trans_succ(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    notice = Receive_notice(driver)
    notice.login("01002","000000")
    notice.send("2","5","7")

