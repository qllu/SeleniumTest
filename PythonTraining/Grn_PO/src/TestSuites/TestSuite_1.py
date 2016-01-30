#coding=utf-8
'''
Created on 2015年9月2日
@author: QLLU
用来分别执行测试用例

'''

import HTMLTestRunner
import unittest, os, sys, time

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")
sys.path.append(os.getcwd()+"src/")

#引用测试用例文件
from TestCases import QT_Space_create_public_space
from TestCases import QT_Space_create_private_space
from TestCases import QT_Space_create_space_category
from TestCases import QT_Space_create_discussion

# 测试用例集合
testnames = [
    QT_Space_create_space_category.CreateSpaceCategory,
    QT_Space_create_public_space.CreatePublicSpace,
    QT_Space_create_private_space.CreatePrivateSpace,
    QT_Space_create_discussion.CreateDiscussion
]


suite = unittest.TestSuite()

# 文件名.类名

for test in testnames:
    suite.addTest(unittest.makeSuite(test))

now = time.strftime("%Y%m%dT%H%M%S_",time.localtime(time.time()))
filename = '../Report/' + now + 'result.html' #测试报告路径

print filename
fp = file(filename, 'wb')

# 添加测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'Result',
                                       description = 'Test_Result：')
runner.run(suite)


