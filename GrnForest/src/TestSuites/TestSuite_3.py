#coding=utf-8
'''
Created on 2015年9月2日
@author: QLLU
用来执行测试用例中的具体方法

'''

import HTMLTestRunner
import unittest, os, sys, time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")
sys.path.append(os.getcwd()+"src/")
sys.path.append(os.getcwd()+"/PythonTest/src/")

#引用测试用例文件
# from TestCases import QT_login_grn
from TestCases.QT_Space_create_space_category import CreateSpaceCategory
from TestCases.QT_Space_create_public_space import CreatePublicSpace
from TestCases.QT_Space_create_private_space import CreatePrivateSpace


class TestSuite_3():

    def test(self):

        if __name__ == '__main__':
            # 构造测试集
            suite = unittest.TestSuite()
            # suite.addTest(unittest.makeSuite(QT_login_grn.LoginGrn) #方法2，文件名.类名
            # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestSuite_1))

            suite.addTest(CreateSpaceCategory('test_create_space_category'))
            suite.addTest(CreatePublicSpace('test1_create_public_space'))
            suite.addTest(CreatePrivateSpace('test1_create_private_space'))

            now = time.strftime("%Y%m%dT%H%M%S_",time.localtime(time.time()))
            filename = '../Report/' + now + 'result.html' #测试报告路径

            print filename
            fp = file(filename, 'wb')

            # 添加测试报告
            runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'Result',
                                                   description = 'Test_Result：')
            runner.run(suite)

            # 运行测试用例集
            # runner = unittest.TextTestRunner()
            # runner.run(suite)

if __name__ == "__main__":
    TestSuite_1().test()


