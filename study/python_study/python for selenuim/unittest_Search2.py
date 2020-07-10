__author__ = 'mingyu.zhang'

#_*_ utf-8 _*_

from selenium import webdriver
import unittest

class SearchTest2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser=webdriver.Chrome()
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()
        cls.browser.get("http://www.baidu.com")

    def test_search2(self):
        self.input=self.browser.find_element_by_id('kw')
        self.input.clear()
        self.input.send_keys('假日')
        self.input.submit()

        self.products=self.browser.find_elements_by_xpath("//div[contains(@class,'c-abstract')]")
        print(self.products.__len__())
        self.assertTrue(bool(self.products))


    @classmethod
    def tearDownClass(cls):
       #cls.browser.quit()
        pass

if '__name__' == '__main__':
    unittest.main(verbosity=2)