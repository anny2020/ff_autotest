# @Time: 2020/4/1  10:03
#登录页面
from common.base import Base
from selenium import webdriver
import time
class LoginPage():
#初始化登录页面中用到的参数,对base进行实例化
    def __init__(self,driver):
        #对导入的base进行实例化
        self.base = Base(driver)
        self.driver = driver
        #定位用户名元素的参数
        self.loc_user = ("id","txtUserName")
        #定位密码元素的参数
        self.loc_pwd = ("id","txtPassWord")
        #定位登录按钮元素的参数
        self.button = ("id","btnSubmit")
        #定位登录成功后首页右上角出现的用户名
        self.home_page_username = ("id","userName")

#定义输入用户名方法
    def input_username(self,user_name):
        self.user_name = user_name
        self.base.send_key(self.loc_user,self.user_name)

#定义输入密码方法
    def input_pwd(self,user_pwd):
        self.user_pwd = user_pwd
        self.base.send_key(self.loc_pwd,self.user_pwd)

#定义点击登录方法
    def click_submit(self):
        self.base.click(self.button)

#获取登录后右上角的用户名
    def get_login_username(self):
        try:
            ele = self.base.findElement(self.home_page_username)
            username = ele.text
            return username
        except:
            return ""

#判断元素是否包含文本
    def is_login_sucess(self,text):
        result = self.base.is_text_in_element(self.home_page_username,text)
        return result

#判断是否存在alert弹窗，有的话就关闭，没有就忽略
    def is_alert_exist(self):
        result = self.base.is_alert_exist()
        if result:
            result.accept()
        else:
            pass


#下面是该文件的测试用代码
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    login_page = LoginPage(driver)
    login_page.input_username("00000")
    login_page.input_pwd("000000")
    login_page.click_submit()
    time.sleep(3)
    result = login_page.get_login_username()
    print(result)
