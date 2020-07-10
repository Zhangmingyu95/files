__author__ = 'mingyu.zhang'

from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):



    def user_login_verify(self,username='',password=''):
        login(self.driver).login_login(username,password)

    def test_login1(self):
        '''
        用户名与密码为空
        :return:
        '''
        self.user_login_verify()
        po=login(self.driver)
        self.assertNotEqual(po.driver.title,"统一应用平台",msg="没有登录成功")
        function.insert_img(self.driver,'test1.png')

    def test_login2(self):
        '''
        用户名为空
        :return:
        '''
        self.user_login_verify(username='')
        po=login(self.driver)
        self.assertNotEqual(po.driver.title,"统一应用平台",msg="没有登录成功")
        function.insert_img(self.driver,'test1.png')

if __name__ == '__main__':
    unittest.main()



