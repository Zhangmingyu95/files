__author__ = 'mingyu.zhang'
#_*_ coding:utf-8 _*_

import  unittest
import  HTMLTestRunner
import os
import unittest_Search2
import unittest_Search
from unittest_Search import SearchTest
from unittest_Search2 import  SearchTest2
from datetime import datetime

now=datetime.now()
datestr=now.strftime("%H-%M-%S-%m-%d-%yy")

dir=os.getcwdb().decode('gbk')

test1=unittest.TestLoader().loadTestsFromModule(unittest_Search)
test2=unittest.TestLoader().loadTestsFromModule(unittest_Search2)

testSuit1=unittest.TestSuite([test1,test2])

filepath=dir + "/SmokeTestReport{}.html".format(datestr)
with  open(filepath,'wb') as outfile:
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Title:Test Report',description='Dose:Smoke')
    runner.run(testSuit1)

