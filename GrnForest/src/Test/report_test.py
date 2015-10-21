#coding=utf-8
'''
Created on 2015年9月4日

@author: QLLU
'''

import unittest
import HTMLTestRunner
from TestCases.GrnLogin import Login

# import sys
# import StringIO
 
class Testlist(unittest.TestCase):
    def test_1(self):
        print "test1"
    def test_2(self):
        print "test2"
  
def suiting():
    filename ="d:\\result.html"
    fp = file(filename,"wb")
    suit = unittest.TestSuite()
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Testlist))
    '''
    suit.addTest(Testlist('test_1'))
    suit.addTest(Testlist('test_2'))
    suit.addTest(unittest.makeSuite(Login)) 
    '''
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="testing result",description="trying")
    runner.run(suit)
#     fp.close()

suiting()

