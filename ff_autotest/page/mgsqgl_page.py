# @Time: 2020/4/9  15:15
from common.base import Base
from selenium import webdriver
import time

class Mgsqgl():
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
        #定位导航菜单敏感时期管理
        self.menu_mgsqgl = ("css selector",".nav-minganshiqi-n>a>cite>p")
        #新增敏感时期按钮
        self.loc_add_mgsq = ("id","btnAddMgsq")
        #新增敏感时期：名称
        self.loc_add_mgsq_mc = ("id","mc")
        #新增敏感时期：有效期始
        self.loc_add_mgsq_yxqs = ("id","yxqs")
        #新增敏感时期：有效期止
        self.loc_add_mgsq_yxqz = ("id","yxqz")
        #日历选择框中：现在
        self.loc_date_now = ('css selector','.laydate-btns-now')
        #日历选择框中：4-30
        self.loc_date_other = ('xpath',".//*[@id='layui-laydate2']/div[1]/div[2]/table/tbody/tr[5]/td[5]")
        #敏感时期类型：
        self.loc_mgsqlx = ("css selector",".layui-input.layui-unselect")
        #敏感时期类型：普通涉访人员
        self.loc_ptsfry = ("css selector",".layui-unselect.layui-form-select.layui-form-selected>dl:nth-child(2)")
        #敏感时期弹窗：保存按钮
        self.loc_save = ("xpath","html/body/div[1]/form/div[5]/a")
        #敏感时期弹窗：关闭按钮
        self.loc_close = ("xpath","html/body/div[1]/form/div[5]/button")
        #是否设置预警值弹窗：确定按钮
        self.loc_yj_confirm = ("xpath",".//*[@id='layui-layer3']/div[3]/a[1]")
        #是否设置预警值弹窗：取消按钮
        self.loc_yj_cancel = ("xpath",".//*[@id='layui-layer3']/div[3]/a[2]")
        #设置预警值弹窗窗口id，用于判断这个窗口是否打开了
        self.loc_yj_mc = ("id","mc")
        #-------------------预警设置页面------------------------
        #设置预警值：蓝色预警
        self.loc_yjfz_lsyj = ("xpath",".//*[@id='yjFz']/li[1]/div/input")
        #设置预警值：提交按钮
        self.loc_szyjz_submit = ("css selector",".submit_btn")
        #提交提示   /删除成功提示共用
        self.submit_tips = ("css selector",".layui-layer-content.layui-layer-padding")
        #点击列表页的查看按钮
        self.loc_list_view = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('tbody')[0].getElementsByTagName('a')[0].click()'''
        #------------------查看弹窗 ------------------
        #title  与查看报告共用
        self.loc_title = ("css selector",".layui-layer-title")
        #-----------------编辑弹窗--------------------
        self.loc_list_edit = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('tbody')[0].getElementsByTagName('a')[1].click()'''
        #---编辑弹窗：提交按钮
        self.loc_edit_submit = ("css selector",".layui-btn")
        #----------------人员导入---------------
        self.loc_list_import = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('tbody')[0].getElementsByTagName('a')[2].click()'''
        #-人员导入：管控来源
        self.loc_gkly = ("css selector",".layui-unselect.layui-form-select")
        # 管控来源下拉选项：
        self.loc_gabjb = ("css selector",".layui-anim.layui-anim-upbit:nth-child(2)")
        #导入文件
        self.loc_file = ("id","file")
        #提交按钮
        self.loc_import_submit = ("css selector",".layui-btn")
        #导入结果提示框标题
        self.loc_import_mess_title = ("css selector",".layui-layer-title")
        #-----------列表：删除按钮----
        self.loc_list_delete = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('tbody')[0].getElementsByTagName('a')[3].click()'''
        #删除提示框:确定删除按钮
        self.loc_dele_butn = ("css selector",".layui-layer-btn0")
        #-----------列表：查看报告按钮-----
        self.loc_view_report = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('tbody')[0].getElementsByTagName('a')[4].click()'''




#登录帐号
    def login(self,username,passwd):
        self.base.send_key(self.loc_user,username)
        self.base.send_key(self.loc_pwd,passwd)
        self.base.click(self.button)

#进入敏感时间管理列表页,“新增敏感时期”
    def mgsqgl_list(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_mgsqgl)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.base.click(self.loc_add_mgsq)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("layui-layer-iframe2")
        time.sleep(2)
        self.base.send_key(self.loc_add_mgsq_mc,"国庆节")
        self.base.click(self.loc_add_mgsq_yxqs)
        self.base.click(self.loc_date_now)
        self.base.click(self.loc_add_mgsq_yxqz)
        self.base.click(self.loc_date_other)
        self.base.click(self.loc_mgsqlx)
        self.base.click(self.loc_ptsfry)


#新增敏感时期后，点击“保存”
    def mgsqgl_save(self):
        self.base.click(self.loc_save)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(1)
        time.sleep(2)

#新增敏感时期后，点击“关闭”
    def mgsqgl_close(self):
        self.base.click(self.loc_close)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(1)

#是否出现“是否设置预警值”的弹窗
    def is_set_early_warn(self):
        try:
            ele = self.base.findElement(self.loc_yj_confirm)
            return True
        except:
            return False

#将新增敏感时期保存后，弹出是否进行预警值设置的点击按钮单独提出来，便于后续分别调用
#点击取消按钮
    def mgsqgl_qxyj(self):
        self.base.click(self.loc_yj_cancel)

#点击确定按钮
    def mgsqgl_jryj(self):
        self.base.click(self.loc_yj_confirm)


#是否进入设置预警值的页面，用于判断新增敏感时期并保存后是点击确定成功进入了预警值设置，还是点击取消成功未进入预警值设置
    def is_open_early_warn(self):
        try:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(2)
            ele = self.base.findElement(self.loc_yj_mc)
            return True
        except:
            return False

#设置预警值，修改了蓝色预警值,提交
    def szyjz(self,value):
        self.base.clear(self.loc_yjfz_lsyj)
        self.base.send_key(self.loc_yjfz_lsyj,value)
        self.base.click(self.loc_szyjz_submit)
        self.driver.switch_to.default_content()

#是否提交成功  此方法未用上，因为提示太短，获取不到
    def is_submit_success(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result

#点击列表上的查看按钮
    def click_view(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_mgsqgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_list_view)
        self.driver.switch_to.default_content()

#点击列表上的编辑按钮
    def click_edit(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_mgsqgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_list_edit)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)

#判断弹窗的标题文本是否包含“查看”，返回True或False
    def get_title(self,text):
        result = self.base.is_text_in_element(self.loc_title,text)
        return result
#编辑弹窗的标题文本获取为空，所以使用获取窗口中的“提交按钮”文本作为判断
    def get_submit_text(self,text):
        result = self.base.is_text_in_element(self.loc_edit_submit,text)
        return result

#人员导入操作
    def import_mem(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_mgsqgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_list_import)
        self.driver.switch_to.frame(2)
        self.base.click(self.loc_gkly)
        self.base.click(self.loc_gabjb)
        self.base.send_key(self.loc_file,r"C:\Users\Ling\Downloads\lksfmb.xlsx")
        self.base.click(self.loc_import_submit)
        self.driver.switch_to.default_content()

    #获取导入结果
    def get_import_result(self,text):
        result = self.base.is_text_in_element(self.loc_import_mess_title,text)
        return result

#删除敏感时期
    def delete(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_mgsqgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_list_delete)
        self.driver.switch_to.frame(1)
        self.base.click(self.loc_dele_butn)
        self.driver.switch_to.default_content()

    #删除敏感时期成功
    def del_success(self,text):
        result = self.base.is_text_in_element(self.submit_tips,text)
        return result

    #查看报告
    def view_report(self):
        self.base.click(self.nav_left)
        time.sleep(2)
        self.base.click(self.menu_mgsqgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_view_report)
        self.driver.switch_to.default_content()




if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    driver.delete_all_cookies()
    driver.refresh()
    mgsqgl = Mgsqgl(driver)
    mgsqgl.login("01003","000000")
    result = mgsqgl.view_report()
