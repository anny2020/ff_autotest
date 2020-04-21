# @Time: 2020/4/1  10:06
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Base():
#初始化参数driver,timeout,t
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5
#定义查找元素的方法
    def findElement(self,locator):
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x :x.find_element(*locator))
        return ele
#定义查找一组元素的方法
    def findElements(self,locator):
        eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x :x.find_elements(*locator))
        return eles
#定义录入值的方法
    def send_key(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)
#定义单击的方法
    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()
#定义找到的元素中包含的文本
    def is_text_in_element(self,locator,text):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return ele
        except:
            return False
#定义判断弹窗是否存在的方法
    def is_alert_exist(self):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            return ele
        except:
            return False
#定义下拉选择框的方法
    def is_selected(self,locator,text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

#定义判断一个元素是否可点击的,可点击要满足既是显示的又是可用的
    def is_clickable(self,locator):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.element_to_be_clickable(locator))
            return ele
        except:
            return False

#等待掩盖的div消息
    def wait_div_disappear(self,locator):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.invisibility_of_element_located(locator))
            return ele
        except:
            return False
#判断单选按钮是否被选中，如果被选中,把值返回
    def is_radio_button_choosed(self,locator):
        ele = self.findElement(locator)
        result = ele.is_selected()
        return result

#清空字段内容
    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()




