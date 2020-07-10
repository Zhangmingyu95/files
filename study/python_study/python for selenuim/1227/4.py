__author__ = 'mingyu.zhang'

from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.set_window_size(600,600)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('kw').submit()
sleep(2)

js='window.scrollTo(300,600)'
driver.execute_script(js)
sleep(2)
driver.get_screenshot_as_file('C:\\User\\mingyu.zhang\\desktop\\hello world.png')
