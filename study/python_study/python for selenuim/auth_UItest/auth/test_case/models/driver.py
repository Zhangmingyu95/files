__author__ = 'mingyu.zh'

from selenium import webdriver
from selenium.webdriver import remote

def browser():
    driver= webdriver.Chrome()

    return  driver

if __name__ =='__main__':
    url='https://auth-sit-ui.uihcloud.cn/'
    dr=browser()
    dr.get(url)
    dr.quit()

