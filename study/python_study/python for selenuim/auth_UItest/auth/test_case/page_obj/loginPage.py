__author__ = 'mingyu.zhang'

from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''
    url='/'

    #Action
    login_username_loc=(By.XPATH,"//*[@type = 'text' and @id = 'name' and @name = 'userName']")
    login_password_loc=(By.XPATH,"//*[@type = 'password' and @id = 'pwd' and @name = 'passWord']")
    login_enter_loc=(By.XPATH,"//*[@id='outer']/div[1]/div[3]/div[1]/button")

    def login_inputName(self,username='admin@uihcloud.cn'):
        '''
        输入用户名
        :param username:
        :param password:
        :return:
        '''
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_inputPassword(self,password='uihimaging@8080'):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_clickLoginButton(self):
        '''
        点击登录按钮
        :return:
        '''
        self.find_element(*self.login_enter_loc).click()

    def login_login(self,username='admin@uihcloud.cn',password='uihimaging@8080'):
        self.open()
        self.login_inputName(username)
        self.login_inputPassword(password)
        self.login_clickLoginButton()




