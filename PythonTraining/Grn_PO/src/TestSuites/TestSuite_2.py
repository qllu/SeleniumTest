#coding=utf-8
'''
Created on 2015年9月2日
@author: QLLU
用来执行TestCases目录中所有以QT开头的测试用例

'''

import HTMLTestRunner
import unittest, os, sys, time

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")
sys.path.append(os.getcwd()+"src/")

#引用测试用例文件
cases_direc = '../TestCases/'
def suite1():
    suite = unittest.TestSuite()
    # 定义discover方法
    discover = unittest.defaultTestLoader.discover(
        cases_direc, pattern='QT_*.py', top_level_dir=None)

    # discover方法筛选出用例，循环添加到测试套件中
    for test_suite in discover:
        for test_cases in test_suite:
            suite.addTests(test_cases)
            # print suite
    return suite

alltests = suite1()

now = time.strftime("%Y%m%dT%H%M%S_",time.localtime(time.time()))
filename = '../Report/' + now + 'result.html' #测试报告路径

print filename
fp = file(filename, 'wb')

# 添加测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'Result',
                                       description = 'Test_Result：')
runner.run(alltests)

