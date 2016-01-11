#coding=utf-8
'''
Created on 2015年9月2日
@author: QLLU
'''

import HTMLTestRunner
import unittest, os, sys, time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")
# sys.path.append(os.getcwd()+"src/")
sys.path.append(os.getcwd()+"/PythonTest/src/")

#引用测试用例文件
# from TestCases.QT_login_grn import LoginGrn
import TestCases.QT_login_grn

suite = unittest.TestSuite()

# suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestSuite_1))
# suite.addTest(LoginGrn('test_login_grn'))
suite.addTest(unittest.makeSuite(TestCases.QT_login_grn.LoginGrn))  #方法2，文件名.类名

now = time.strftime("%Y%m%dT%H%M%S_",time.localtime(time.time()))
filename = '../Report/' + now + 'result.html' #测试报告路径
# filename = 'd:\\' + now + 'result.html' #测试报告路径

print filename
fp = file(filename, 'wb')

# 添加测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'Result',
                                       description = 'Test_Result：')
runner.run(suite)


# 运行测试用例集
# runner = unittest.TextTestRunner()
# runner.run(suite)
