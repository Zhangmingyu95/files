__author__ = 'mingyu.zhang'

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")
driver.get("http://news.baidu.com")
driver.back()
driver.forward()
driver.implicitly_wait(10)

