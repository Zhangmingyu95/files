__author__ = 'mingyu.zhang'
# _*_ utf-8 _*_

from selenium import webdriver

browser = webdriver.Chrome()
print(1)
browser.maximize_window()
print(2)
browser.get('http://www.baidu.com')
print(3)
input_search_keyword=browser.find_element_by_id("kw")
button_search=browser.find_element_by_id('su')
input_search_keyword.clear()
input_search_keyword.send_keys('selenium')
button_search.click()
#input_search_keyword.submit()
result=browser.find_elements_by_id()
