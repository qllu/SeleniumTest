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
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver

class AddOrganization(unittest.TestCase):
    '''
    新增组织
    '''
    def setUp(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")#打开浏览器，并打开forest

    def test_add_organization(self):
        
        #读取测试数据     
        dataoper = DataReader('QT_System_add_organization.xml')

        #登录用户
        Operations().login(dataoper.readxml('login', 0, 'username'),dataoper.readxml('login', 0, 'password'))
        driver.wait(3)

        #点击进入共通管理
        admin_url = driver.testurl("qatest01") + "/admin/"
        driver.geturl(admin_url)
        driver.wait(3)

        #点击进入组织
        driver.click('byxpath', dataoper.readxml('org', 0, 'org_link'))
        driver.wait(3)

        #点击添加组织按钮
        driver.click('byid', dataoper.readxml('org', 0, 'add_botton'))

        #输入组织名
        driver.input('byid', dataoper.readxml('org', 0, 'org_name'), dataoper.readxml('org', 0, 'name'))
        driver.wait(2)

        # #输入组织代码
        # driver.input('byid', dataoper.readxml('org', 0, 'org_code'), dataoper.readxml('org', 0, 'code'))
        # driver.wait(2)

        #输入组织说明
        driver.input('byid', dataoper.readxml('org', 0, 'org_comment'), dataoper.readxml('org', 0, 'comment'))
        driver.wait(2)

        #保存
        driver.click('byid', dataoper.readxml('org', 0, 'save'))
        driver.wait(3)

        #验证(云版未验证)
        # checkpoint1 = driver.gettext('bycss',dataoper.readxml('login', 0,'checkpoint'))
        # value1 = dataoper.readxml('login', 0, 'value')
        # self.assertEqual(checkpoint1,value1)

        #退出
        Operations().logout()
        driver.wait(5)

        
    def tearDown(self):
        driver.close()#关闭浏览器
       
if __name__ == "__main__":   
    unittest.main()
