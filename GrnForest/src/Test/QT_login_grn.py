#coding=utf-8
'''
Created on 2015年8月12日

@author: QLLU
'''
# from lib2to3.pgen2.driver import Driver
# import xml.dom.minidom
import time,unittest
import sys,os
sys.path.append("..")
sys.path.append(os.getcwd()+"/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp


# 导入需要的公共函数类
class LoginGrn(unittest.TestCase):
    """
    登录检测，更换用户登录
    """
    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("fcn")#打开浏览器，并打开forest

    def test_login_grn(self):

        # 读取测试数据
        dataoper = DataReader('QT_login_grn.xml')

        # 登录用户
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),dataoper.readxml('login', 0, 'password'))

        # 进入Garoon
        grn_url = "https://qatest01.cybozu.cn/g/"
        WebDriverHelp().geturl(grn_url)

        # 点击用户下拉菜单
        WebDriverHelp().clickitem('byid', dataoper.readxml('login', 0, 'item'))
               
        checkpoint1 = WebDriverHelp().gettext('bycss',dataoper.readxml('login', 0,'checkpoint'))
        value1 = dataoper.readxml('login', 0, 'value')        
        self.assertEqual(checkpoint1,value1)


        # 退出
        QT_Operations().logout()
        time.sleep(3) 

        """
        #设置起始节点为0，循环2次
        num = 0
        while num < 2:        
            #登录用户
            QT_Operations().login(dataoper.readxml('login', num, 'username'),dataoper.readxml('login', num, 'password'))  
            #点击用户下拉菜单
            WebDriverHelp().clickitem('byid', dataoper.readxml('login', num, 'item'))
                   
            checkpoint1 = WebDriverHelp().gettext('bycss',dataoper.readxml('login', num,'checkpoint'))
            value1 = dataoper.readxml('login', num, 'value')        
            self.assertEqual(checkpoint1,value1) 
            #退出
            QT_Operations().logout()
            time.sleep(3)
                        
            num = num + 1  
        """
        
    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器
if __name__ == "__main__":
    unittest.main()
