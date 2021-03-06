# # @Time: 2020/4/16  15:48
# import unittest
# from common.HTMLTestRunner_cn import HTMLTestRunner
# import time
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# import os
# #当前脚本所在文件真实路径
# cur_path = os.path.dirname(os.path.realpath(__file__))
#
# def add_case(caseName="case",rule="test*.py"):
#     '''第一步：加载所有的测试用例'''
#     case_path = os.path.join(cur_path,caseName)#用例文件夹  os.path.join是把目录和文件名合成一个路径
#     #如果不存在这个case文件夹，就自动创建一个（os.path.exists如果路径case_path存在，返回True,不存在返回False）
#     if not os.path.exists(case_path):os.mkdir(case_path)
#     print("test case path:%s"%case_path)
#     #定义discover方法的参数
#     discover = unittest.defaultTestLoader.discover(start_dir=case_path,pattern=rule)
#     print(discover)
#     return discover
#
# def run_case(all_case,reportName="report"):
#     '''第二步：执行所有的用例，并把结果写入HTML测试报告'''
#     now = time.strftime('%Y-%m-%d %H_%M_%S')
#     report_path = os.path.join(cur_path,reportName) #用例文件夹
#     #如果不存在这个report文件夹，就自动创建一个
#     if not os.path.exists(report_path):os.mkdir(report_path)
#     # report_abspath = os.path.join(report_path,now+"result.html") #为了测试Jenkins发布报告先注掉
#     #为了在jenkins中展示，先去掉时间进行测试
#     report_abspath = os.path.join(report_path,"index.html") #为了测试jenkins先添加
#     print("report path:%s"%report_abspath)
#     fp = open(report_abspath,"wb")
#     runner = HTMLTestRunner(stream=fp,title='自动化测试报告，测试结果如下：',description='用例执行情况')
#     #调用add_case函数返回值
#     runner.run(all_case)
#     fp.close()
#
# def get_report_file(report_path):
#     '''第三步：获取最新的测试报告'''
#     # lists = os.listdir(report_path)
#     # lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path,fn)))
#     # print(u"最新测试生成的报告: "+lists[-1])
#     #找到最新生成的报告
#     # report_file = os.path.join(report_path,lists[-1]) #为了测试jenkins构建成功并发布report,先注掉
#     report_file = os.path.join(report_path,"index.html")#为了测试先添加此行
#     return report_file
#
#
# def send_email(sender,psw,receiver,smtpserver,report_file,port):
#     with open(report_file,"rb") as f:
#         mail_body = f.read()
#     #定义邮件内容
#     msg = MIMEMultipart()
#     body =  MIMEText(mail_body,_subtype='html',_charset='utf-8')
#     msg['Subject'] = u"自动化测试报告"
#     msg["from"] = sender
#     if isinstance(receiver,str):
#         msg["to"] = receiver
#     if isinstance(receiver,list):
#         msg["to"] = ",".join(receiver)
#     msg.attach(body)
#     #添加附件
#     att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename="report.html"'
#     msg.attach(att)
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)  #连服务器
#         smtp.login(sender,psw)
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver,port)
#         smtp.login(sender,psw)   #登录
#     smtp.sendmail(sender,receiver,msg.as_string())
#     smtp.quit()
#     print("test report email has send out")
#
# if __name__ == '__main__':
#     all_case = add_case() #1加载用例
#     run_case(all_case)   #2执行用例
#     #获取最新的测试报告文件
#     report_path = os.path.join(cur_path,"report")    #用例文件夹
#     report_file = get_report_file(report_path)       #3获取最新的测试报告
#     sender = "18537810265@163.com"
#     psw = "********"
#     smtp_server = "smtp.163.com"
#     port = 465
#     receiver = "714552125@qq.com"
#     # send_email(sender,psw,receiver,smtp_server,report_file,port)



import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner

case_path = r"E:\PycharmProjects\ffyj\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=case_path,pattern=rule)
print(discover)

#report_path = r"E:\PycharmProjects\ffyj\report\report"+".html"
report_path = r"E:\PycharmProjects\100days\test\workspace\ff_autotest\ff_autotest\report\report"+".html"
fp = open(report_path,'wb')

runner = HTMLTestRunner(stream=fp,title='报告名称',description='描述')
runner.run(discover)
fp.close()

