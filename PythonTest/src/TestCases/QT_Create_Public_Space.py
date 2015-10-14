#coding=utf-8
'''
Created on 2015年10月9日

@author: QLLU
'''
#导入需要的公共函数类
import time,unittest,sys,os
sys.path.append("..")
sys.path.append(os.getcwd()+"/src/")
from CommonFunction.DataOperations import DataOperations
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp

class testcases_create_public_space(unittest.TestCase):
    '''
    新增space目录
    '''
    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("fcn")#打开浏览器，并打开forest

    def test_create_public_space(self):

        #读取测试数据
        dataoper = DataOperations('QT_Create_Public_Space.xml')

        #登录用户
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),dataoper.readxml('login', 0, 'password'))
        time.sleep(2)

        #点击进入garoon各应用程序管理
        garoon_url = "https://qatest01.cybozu.cn/g/"
        WebDriverHelp().geturl(garoon_url)
        time.sleep(2)

        #点击进入space
        WebDriverHelp().clickitem('bycss', dataoper.readxml('space', 0, 'space_icon'))
        time.sleep(2)

        #创建space
        WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, 'creat_link'))
        time.sleep(2)
        #输入title
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'space_title'), dataoper.readxml('space', 0, 'title'))
        time.sleep(1)
        #搜索添加用户
        WebDriverHelp().inputvalue('byname', dataoper.readxml('space', 0, 'e_keyword'), dataoper.readxml('space', 0, 'keyword'))
        time.sleep(2)
        WebDriverHelp().clickitem('byxpath', dataoper.readxml('space', 0, 'search'))
        time.sleep(2)
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'add_user'))
        time.sleep(2)
        #选择公开方式
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'public'))

        #保存
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(2)

        #进入详细页面
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'droplist'))
        time.sleep(2)
        WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, 'detail'))
        time.sleep(2)

        #验证
        check = WebDriverHelp().gettext('bycss', dataoper.readxml('space', 0,'check'))
        # print "check:" + check
        value = dataoper.readxml('space', 0, 'value')
        # value = dataoper.readxml('space', 0, 'value2')
        # print "value:" + value
        self.assertEqual(check,value)
        # self.assertEqual(check2,value2)

        #退出
        QT_Operations().logout()
        time.sleep(3)


    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器

if __name__ == "__main__":
    unittest.main()
