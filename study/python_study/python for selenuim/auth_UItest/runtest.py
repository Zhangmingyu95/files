__author__ = 'mingyu.zhang'

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import  smtplib
import unittest
import time
import os


#==============================发送邮件
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告","utf-8")

    smtp=smtplib.SMTP("smtp.united-imaging.com")
    smtp.starttls()
    smtp.login("mingyu.zhang@united-imaging.com",'Kevin987654321')
    smtp.sendmail("mingyu.zhang@united-imaging.com","mingyu.zhang@united-imaging.com",msg.as_string())
    smtp.quit()
    print('mail has send out')



#========================生成报告
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+'\\'+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    tm=time.strftime("%y-%m-%d_%H_%M")
    tm=str(tm)
    filename='./'+tm+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='testreport')
    discover=unittest.defaultTestLoader.discover('./auth/test_case/',pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path=new_report('./')
    send_mail(file_path)