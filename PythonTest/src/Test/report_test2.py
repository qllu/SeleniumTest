#coding=utf-8
'''
Created on 2015年9月6日
http://bbs.51testing.com/thread-1067282-1-1.html

目的：测试HTMLTestRunner报告是否能生成

问题：在sublime中，测试能正常生成报告；但eclipse+pydev不能生成

疑点：
1.pydev的版本问题？当前版本2.8.2.2013090511，是否需要更高版本
2.eclipse的编码问题？eclipse中编码已设置为utf-8

@author: QLLU
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import HTMLTestRunner 

class Bing(unittest.TestCase):
    
    def setUp(self):
        print "test"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.bing.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_bing_search(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("sb_form_q").send_keys("selenium webdriver")
        driver.find_element_by_id("sb_form_go").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    print "test"
    testunit = unittest.TestSuite()    
    testunit.addTest(Bing("test_bing_search"))
    now = time.strftime("%Y%m%d_%H%M%S_",time.localtime(time.time()))
    print now
    filename = "E:\\" + now + 'report_test2.html'
    print filename
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u'必应搜索测试报告',
                                       description=u'用例执行情况：')

    runner.run(testunit)
    fp.close()   
    
    