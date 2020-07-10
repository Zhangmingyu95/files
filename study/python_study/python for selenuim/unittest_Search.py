__author__ = 'mingyu.zhang'

#_*_ utf-8 _*_

import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser=webdriver.Chrome()
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()
        cls.browser.get('http://www.baidu.com')

    def test_search_keyword(self):
        self.input=self.browser.find_element_by_id('kw')
        self.input.clear()
        self.input.send_keys('selenium')
        self.input.submit()

        self.result=self.browser.find_elements_by_xpath("//div[contains(@class,'c-abstract')]")
        print(len(self.result))
        self.assertTrue(bool(self.result))

    def test_search_keyword2(self):
        self.input=self.browser.find_element_by_id('kw')
        self.input.clear()
        self.input.send_keys('python')
        self.input.submit()

        self.result=self.browser.find_elements_by_xpath("//div[contains(@class,'c-abstract')]")
        print(len(self.result))
        self.assertTrue(bool(self.result))

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if '__init__'=='__main__':
    unittest.main(verbosity=2)