__author__ = 'mingyu.zhang'

from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

print('before login =========')

title=driver.title
url=driver.current_url
print('title=%s url=%s' % (title,url) )

print('start your test')

kw=driver.find_element_by_id('kw')
kw.clear()
kw.send_keys('selenium')
su=driver.find_element_by_id('su')
su.clear()
su.click()
sleep(3)

print("operation is done")

title=driver.title
url=driver.current_url
print('title=%s url=%s' % (title,url) )