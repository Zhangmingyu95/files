__author__ = 'mingyu.zhang'

from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.delete_all_cookies()
driver.add_cookie({'name':'key-aaa','value':'value-aaa'})
for cookie in driver.get_cookies():
    print("%s-->%s" % (cookie['name'],cookie['value']))
print('=======================')
driver.delete_cookie('key-aaa')
for cookie in driver.get_cookies():
    print("%s-->%s" % (cookie['name'],cookie['value']))
driver.quit()