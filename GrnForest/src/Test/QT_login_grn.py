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
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


# 导入需要的公共函数类
class LoginGrn(unittest.TestCase):
    """
    登录检测，更换用户登录
    """
    def setUp(self):
        WebDriver("open","firefox","local").open("qatest01")#打开浏览器，并打开forest

    def test_login_grn(self):

        # 读取测试数据        

        # 登录用户
        Operations().login("q1", "cybozu2")

        # 进入Garoon
        grn_url = "https://qatest01.cybozu.cn/g/mail/index.csp?"
        WebDriver().geturl(grn_url)
        WebDriver().click("bylink", u"发送E-mail")
        time.sleep(2)
        WebDriver().click("bycss", "ul.holder.ui-sortable")
        time.sleep(2)
        WebDriver().clear("bycss", "input.maininput")
        time.sleep(2)
        WebDriver().clear("bycss", "input.maininput")
        WebDriver().input("bycss", "input.maininput", "ynchang@cybozu.net.cn")
        time.sleep(2)
        WebDriver().click("bycss", "input.maininput")
        WebDriver().input("byid", "subject_mail", "test")
        WebDriver().click("byclass", "buttonMain-grn")
        WebDriver().click("bycss", "p > input.buttonMain-grn")


        # 退出
        Operations().logout()
        time.sleep(3) 

        """
        #设置起始节点为0，循环2次
        num = 0
        while num < 2:        
            #操作

            num = num + 1  
        """
        
    def tearDown(self):
        WebDriver().close()#关闭浏览器

if __name__ == "__main__":
    unittest.main()
