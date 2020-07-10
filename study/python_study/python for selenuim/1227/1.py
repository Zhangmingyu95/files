__author__ = 'mingyu.zhang'

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

#driver.find_element_by_id("kw").send_keys('1')
#driver.find_element_by_id('su').click()
#sleep(3)
#driver.find_element_by_xpath("//div[@id='content_left']/div[@id='1']/h3/a").click()
#sleep(3)
#driver.refresh()
#text=driver.find_element_by_xpath("//div[@id='content_left']/div[@id='1']/h3/a").text
#print(text)
#size
#print(driver.find_element_by_xpath("//div[@id='content_left']/div[@id='1']/h3/a").get_attribute('href'))
#is_displayed()

#back() 返回上一页
#forward() 前进一页
#ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='u']/a[2]")).perform()
#sleep(3)
#driver.find_element_by_xpath("//*[@class='bdnuarrow']/div/a[@class='setpref']").click()

#sleep(3)
#ActionChains(driver)   选择驱动器作为动作链的输入
#perform()  执行所储存的行为
#context_click()   右击
#double_click()     双击
#drag_and_drop()    拖动
#move_to_element()  鼠标悬停

#element_search=driver.find_element_by_id("kw")
#element_search.send_keys('hahaa')
#sleep(2)
#element_search.send_keys(Keys.BACK_SPACE)
#sleep(2)
#element_search.send_keys(Keys.SPACE)
#element_search.send_keys('aaa')
#element_search.submit()
#Keys.SPACE         键盘的空格输入
#Keys.BACK_SPACE    键盘的回车输入
#Keys.CONTROL,'a'   键盘的全选
#Keys.CONTROL,'v'   键盘的粘贴
#Keys.CONTROL,'c'   键盘的复制
#Key.CONTROL,'x'    键盘的剪切
#Keys.TAB            键盘的换行
#Keys.F1             键盘的F1

'''
浏览器属性
driver.title
driver.current_url
'''

'''
显式元素等待
WebDriverWait(driver,wait_time,fresh_frequency).until(EC.present_of_element_located(By.ID,'kw'))
等待直到元素id=kw出现

隐式元素等待
driver.implicitly_wait(10)
'''

'''
切换frame
switch_to.frame(id/name)
'''

'''
切换窗口
window_1=driver.current_window_handle
window_all=driver.window_handles
for i in window_all:
    if i=window1:
        driver.switch_to_window(i)
'''

'''
警告窗处理
alert=driver.switch_to_alert()
alert.accept()  接受警告
alert.dismiss()    解散警告框
alert.text      返回警告传内容
alert.send_keys('') 向警告框发送文本
'''

'''
上传文件
向input type=file 标签上传
element.send_keys('file_local_url')
'''

'''
操作cookies
driver.get_cookies()    返回所有cookie
driver.get_cookie(name) 返回指定Name的cookie
driver.add_cookie({'name':name,'value':'value'})   添加cookie
driver,delete_cookie(name) 删除cookie
driver.delete_cookies() 删除所有cookies
'''

'''
执行js代码
js=''
driver.execute_script(js)
'''

'''
窗口截图
driver.get_screenshot_as_file('local url')
'''

'''
关掉某个窗口
driver.close()
关闭所有窗口
driver.quit()
'''

'''
读取txt文件
read()      读取整个文件
readline()  读取一行
readlines() 读取所有行
'''

'''
读取csv文件
import csv
date=csv.reader(open('url','r'))
'''

'''
读取xml文件
dom=minidom.parse('info.xml')   打开文件,获得文档对象
root=dom.ducomentElement   获得根元素对象
root.nodeName         元素节点名称
root.nodeValue        元素节点值
root.nodeType           元素节点类型
root.ELEMENT_NODE       元素节点
tag=root.getElementsByTagName('brower') 获得元素
print(tag.tagName)
'''

'''
获得元素的属性值
root=minidom.parse('url').ducumentElement
root.getAttribute('word')
'''

