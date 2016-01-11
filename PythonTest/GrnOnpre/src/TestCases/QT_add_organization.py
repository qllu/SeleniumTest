#coding=utf-8
'''
Created on 2015年10月8日

@author: QLLU
'''

#导入需要的公共函数类
import time
import unittest
import sys,os
sys.path.append("..")
sys.path.append(os.getcwd()+"/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp

class AddOrganization(unittest.TestCase):
    '''
    新增组织
    '''
    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("fcn")#打开浏览器，并打开forest

    def test_add_organization(self):


        
        #读取测试数据     
        dataoper = DataReader('QT_add_organization.xml')

        #登录用户
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),dataoper.readxml('login', 0, 'password'))
        time.sleep(2)

        #点击进入共通管理
        admin_url = "https://qatest01.cybozu.cn/admin/"
        WebDriverHelp().geturl(admin_url)
        time.sleep(2)

        #点击进入组织
        WebDriverHelp().clickitem('byxpath', dataoper.readxml('org', 0, 'org_link'))
        time.sleep(2) 

        #点击添加组织按钮
        WebDriverHelp().clickitem('byid', dataoper.readxml('org', 0, 'add_botton'))

        #输入组织名
        WebDriverHelp().inputvalue('byid', dataoper.readxml('org', 0, 'org_name'), dataoper.readxml('org', 0, 'name'))
        time.sleep(1) 

        # #输入组织代码
        # WebDriverHelp().inputvalue('byid', dataoper.readxml('org', 0, 'org_code'), dataoper.readxml('org', 0, 'code'))
        # time.sleep(1)

        #输入组织说明
        WebDriverHelp().inputvalue('byid', dataoper.readxml('org', 0, 'org_comment'), dataoper.readxml('org', 0, 'comment'))
        time.sleep(1) 

        #保存
        WebDriverHelp().clickitem('byid', dataoper.readxml('org', 0, 'save'))
        time.sleep(2)

        #验证(云版未验证)
        # checkpoint1 = WebDriverHelp().gettext('bycss',dataoper.readxml('login', 0,'checkpoint'))
        # value1 = dataoper.readxml('login', 0, 'value')
        # self.assertEqual(checkpoint1,value1)

        #退出
        QT_Operations().logout()
        time.sleep(3) 

        
    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器
       
if __name__ == "__main__":   
    unittest.main()
