__author__ = 'mingyu.zhang'
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import  smtplib
import unittest
import os

#========================发送邮件===========================
def send_mail(file_new):
    f =open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('自动化测试报告','utf-8')

    smtp = smtplib.SMTP("smtp.united-imaging.com")
    smtp.starttls()
    smtp.login("mingyu.zhang@united-imaging.com",'Kevin987654321')
    smtp.sendmail("mingyu.zhang@united-imaging.com","mingyu.zhang@united-imaging.com",msg.as_string())
    smtp.quit()
    print('email has send out!')


def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ =='__main__':
    test_dir="./"
    test_report='./'

    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    #now=time.strptime("%y-%m-%d_%H_%M_%S")
    filename=test_dir+'result.html'
    fp=open(filename,'wb')

    runner=HTMLTestRunner(stream=fp,title='测试报告',description='nothing')

    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_mail(new_report)