# @Time: 2020/4/2  10:17
#涉访人员管理页面的元素及功能操作方法（申请列管、申请撤管、新增稳控、打击处理）
from common.base import Base
from selenium import webdriver
import time

class Apply_manage():
#初始化涉访管理页面的元素参数
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
        #涉访管理页面中“申请列管”按钮元素
        self.loc_sqlg = ("xpath","html/body/div[1]/div/div/div[2]/div/div[1]/button[1]")
        #申请列管对话框中的“身份证号”
        self.loc_sfzh = ("id","cx_sfzh")
        #申请列管对话框中“查询”按钮，用于查询人员是否存在
        self.loc_cx = ("id","bt_queryRyxx")
        #申请列管对话框中“管控来源”选择框
        self.loc_gkly = ("xpath",".//*[@id='gknr']/div[1]/div[1]/div/div/div/input")
        #“管控来源”下拉框的值“公安部交办”
        self.loc_gabjb = ("xpath",".//*[@id='gknr']/div[1]/div[1]/div/div/dl/dd[2]")
        #"涉访诉求"下拉框
        self.loc_sfsq = ("xpath",".//*[@id='gknr']/div[1]/div[2]/div/div/div/input")
        #"涉访诉求"选项值"婚姻家庭"
        self.loc_hyjt = ("xpath",".//*[@id='gknr']/div[1]/div[2]/div/div/dl/dd[2]")
        #弹窗最大化 非必须，先保留
        # self.loc_win_max = ("css selector",".layui-layer-ico.layui-layer-max")
        #“管控等级”下拉框
        self.loc_gkdj = ("xpath",".//*[@id='gknr']/div[2]/div[1]/div/div/div/input")
        #"管控等级"选项值“A”
        self.loc_A = ("xpath",".//*[@id='gknr']/div[2]/div[1]/div/div/dl/dd[2]")
        #"稳控状态"下拉框
        self.loc_wkzt = ("xpath",".//*[@id='gknr']/div[2]/div[2]/div/div/div/input")
        #“稳控状态”选项值
        self.loc_wkzt_value = ("xpath",".//*[@id='gknr']/div[2]/div[2]/div/div/dl/dd[2]")
        #“联系电话”文本框
        self.loc_phone = ("xpath",".//*[@id='gknr']/div[10]/div[2]/div/input")
        #"当前状态"下拉框
        self.loc_status = ("xpath",".//*[@id='gknr']/div[11]/div/div/div/div/input")
        #“当前状态”选项值
        self.loc_status_value = ("xpath",".//*[@id='gknr']/div[11]/div/div/div/dl/dd[2]")
        #"提交"按钮
        self.submit = ("id","btn")
        #"提交成功提示"
        self.loc_submit_tip = ("css selector",".layui-layer-content.layui-layer-padding")
        #--------------------------------------
        #涉访人员管理列表第一条数据
        self.loc_sfry_list_01 = ("xpath","html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/"
                                         "div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div/i")
        #------------------------新增稳控按钮
        self.loc_xzwk = ("xpath","html/body/div[1]/div/div/div[2]/div/div[1]/button[3]")
        #新增稳控弹窗：稳控时间/与新增打击处理处理时间共同属性
        self.loc_wksj = ("id","test5")
        #新增稳控弹窗：选择时间，确定按钮 /新增打击处理共同弹窗事件
        self.loc_date_comfirm = ("css selector",".laydate-btns-confirm")
        #新增稳控弹窗：稳控地点
        self.loc_location = ("name","wkLocation")
        #新增稳控弹窗：稳控描述
        self.loc_wkdes = ("name","wkDescrition")
        #新增稳控弹窗：涉访人表现
        self.loc_show =("name","ffShow")
        #新增稳控弹窗：备注  /  与新增打击处理共同备注属性 / 与申请撤管共用
        self.loc_remark =("name","remark")
        #新增稳控弹窗：照片 文件上传服务器要确保是正常的才可以，测试时应该是未启动，忽略此步
        # self.loc_relatedPicture = ("name","relatedPicture")
        #新增稳控弹窗：提交按钮
        self.loc_submit = ("xpath","html/body/div[1]/form/div[13]/button[1]")
        #-----------------------------新增打击处理按钮
        self.loc_djcl = ("xpath","html/body/div[1]/div/div/div[2]/div/div[1]/button[4]")
        #新增打击处理：打击处理原因
        self.loc_hitReason = ("name","hitReason")
        #新增打击处理：提交按钮
        self.loc_submit1 = ("xpath","html/body/div[1]/form/div[10]/button[1]")
        #-----------------------------新增撤管按钮
        self.loc_sqcg = ("xpath","html/body/div/div/div/div[2]/div/div[1]/button[2]")
        #新增撤管弹窗：撤管原因选择框
        self.loc_cgyy = ("xpath","html/body/div/form/div[7]/div/div/div/input")
        #新增撤管弹窗：修改撤管原因为其他
        self.loc_cgyy_other = ("xpath","html/body/div/form/div[7]/div/div/dl/dd[3]")
        #新增撤管弹窗：提交按钮
        self.loc_sqcg_submit = ("xpath","html/body/div/form/div[9]/button[1]")
        #列表中“人员档案”操作按钮
        self.loc_archive = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('a')[0].click()'''
        #人员档案弹窗的标题
        self.loc_archive_title = ("css selector",".layui-layer-title")
        #列表中“人员编辑”操作按钮
        self.loc_edit = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('a')[1].click()'''
        #电话：
        self.loc_phone = ("name","lxdh")
        # 人员编辑提交按钮
        self.loc_submit = ("xpath","html/body/div[1]/form/div[11]/button[1]")
        #新增稳控提交按钮
        self.loc_xzwk_submit = ("xpath","html/body/div[1]/form/div[13]/button[1]")
        #获取列表中修改后的管控情况 暂未用
        self.gkqk_value = '''document.getElementsByTagName('iframe')[1].contentWindow.document.
        body.getElementsByTagName('td')[6].getElementsByTagName('div')[0].outerHTML'''




#登录管理员帐号
    def login(self,username,passwd):
        self.base.send_key(self.loc_user,username)
        self.base.send_key(self.loc_pwd,passwd)
        self.base.click(self.button)

#定义申请列管人员信息查询操作方法：点击“涉访管理”菜单-->申请列管-->录入人员身份证号->查询
    def sqlg(self,sfzh,gkly,phone):
        self.base.click(self.loc_sfgl)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.base.click(self.loc_sqlg)
        self.driver.switch_to.default_content()
        # self.base.click(self.loc_win_max)  这个最大化没必要加
        time.sleep(2)
        self.driver.switch_to.frame("layui-layer-iframe2")
        self.base.send_key(self.loc_sfzh,sfzh)
        self.base.click(self.loc_cx)
        self.base.click(self.loc_gkly)
        self.base.click(self.loc_gabjb)
        self.base.click(self.loc_sfsq)
        self.base.click(self.loc_hyjt)
        self.base.click(self.loc_gkdj)
        self.base.click(self.loc_A)
        self.base.click(self.loc_wkzt)
        self.base.click(self.loc_wkzt_value)
        self.base.send_key(self.loc_phone,phone)
        self.base.click(self.loc_status)
        self.base.click(self.loc_status_value)
        self.base.click(self.submit)
        self.driver.switch_to.default_content()


#在涉访人员管理页面，进行新增稳控操作方法：点击涉访人员管理、选中列表第一条数据、点击新增稳控
    def xzwk(self,location,wkdes,show,remark):
        self.base.click(self.loc_sfgl)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.base.click(self.loc_sfry_list_01)
        self.base.click(self.loc_xzwk)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame("layui-layer-iframe2")
        self.base.click(self.loc_wksj)
        time.sleep(2)
        self.base.click(self.loc_date_comfirm)
        self.base.send_key(self.loc_location,location)
        self.base.send_key(self.loc_wkdes,wkdes)
        self.base.send_key(self.loc_show,show)
        self.base.send_key(self.loc_remark,remark)
        time.sleep(2)
        # self.base.send_key(self.loc_relatedPicture,"E:\PycharmProjects\ffyj\page\test.png")
        self.base.click(self.loc_xzwk_submit)
        self.driver.switch_to.default_content()

#在涉访人员管理页面，进行新增稳控操作方法：点击涉访人员管理、选中列表第一条数据、点击新增打击处理
    def djcl(self,hitreason,remark):
        self.base.click(self.loc_sfgl)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.base.click(self.loc_sfry_list_01)
        self.base.click(self.loc_djcl)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame("layui-layer-iframe2")
        self.base.click(self.loc_wksj)
        time.sleep(2)
        self.base.click(self.loc_date_comfirm)
        self.base.send_key(self.loc_hitReason,hitreason)
        self.base.send_key(self.loc_remark,remark)
        time.sleep(2)
        self.base.click(self.loc_submit1)
        self.driver.switch_to.default_content()

#在涉访人员管理页面，进行新增撤管操作方法：点击涉访人员管理、选中列表第一条数据、点击新增撤管
    def sqcg(self,remark):
        self.base.click(self.loc_sfgl)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.base.click(self.loc_sfry_list_01)
        self.base.click(self.loc_sqcg)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame("layui-layer-iframe2")
        self.base.click(self.loc_cgyy)
        self.base.click(self.loc_cgyy_other)
        self.base.send_key(self.loc_remark,remark)
        self.base.click(self.loc_sqcg_submit)

#这个方面对于此页面弹窗提交成功提示是通用的
    def is_submit_success(self,text):
        result = self.base.is_text_in_element(self.loc_submit_tip,text)
        return result

#获取点击查询后的提示内容
    # def get_tips(self):
    #     try:
    #         ele = self.base.findElement(self.loc_tips)
    #         result = ele.result
    #         return result
    #     except:
    #         return null
#点击列表第一条数据的人员档案按钮
    def mem_archive(self):
        self.base.click(self.loc_sfgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_archive)
        self.driver.switch_to.default_content()

#判断打开弹窗的title是不是“人员档案”
    def get_archive_title(self,text):
        result = self.base.is_text_in_element(self.loc_archive_title,text)
        return  result

#点击列表中第一条数据的人员编辑按钮
    def mem_edit(self,phone):
        self.base.click(self.loc_sfgl)
        time.sleep(2)
        self.driver.execute_script(self.loc_edit)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.frame(2)
        time.sleep(2)
        self.base.clear(self.loc_phone)
        self.base.send_key(self.loc_phone,phone)
        self.base.click(self.loc_submit)
        self.driver.switch_to.default_content()

#获取编辑成功提示
    def get_edit_succ(self,text):
        result = self.base.is_text_in_element(self.loc_submit_tip,text)
        return result


#以下为本模块的测试代码
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.30.185:8082/ffyj/login.html")
    sqlg = Apply_manage(driver)
    sqlg.login("01003","000000")
    sqlg.mem_edit("7888888")
    s = sqlg.get_edit_succ("操作成功")
    print(s)




