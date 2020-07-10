__author__ = 'mingyu.zhang'
import unittest
from Account import model
from HTMLTestRunner import HTMLTestRunner

class test_model(unittest.TestCase):
    '''
    测试测试
    '''

    @classmethod
    def setUpClass(cls):
        print('begining')

    def test_add(self):
        self.assertEqual(model().add(),3)

    def test_add2(self):
        '''
        :return:
        '''
        self.assertEqual(model(2,3).add(),5)

    @classmethod
    def tearDownClass(cls):
        print('end')

if __name__ == '__main__':
    unittest.main()
'''
    suite=unittest.TestSuite()
    suite.addTest(test_model('test_add2'))
    fp=open('./testReport.html','wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告')

    runner.run(suite)
    fp.close()
'''

