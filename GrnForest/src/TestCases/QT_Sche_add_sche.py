#coding=utf-8
'''
Created on 2015年8月12日

@author: QLLU
'''
# from lib2to3.pgen2.driver import Driver
import xml.dom.minidom
import time,unittest
import sys,os
sys.path.append("..")
sys.path.append(os.getcwd()+"/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp


#导入需要的公共函数类
class AddSche(unittest.TestCase):
    '''
    登录检测，更换用户登录
    '''
    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("fcn")#打开浏览器，并打开forest
       
    def test_add_sche(self):
        
        #读取测试数据     
        dataoper = DataReader('QT_Sche_add_sche.xml')

        #登录用户
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))

        #进入Garoon
        grn_url = "https://qatest01.cybozu.cn/g/"
        WebDriverHelp().geturl(grn_url)
        time.sleep(2)

        #选择日程
        WebDriverHelp().clickitem('bycss', dataoper.readxml('sche', 0, 'sche_icon'))
        time.sleep(2) 
        #点击日程登录
        WebDriverHelp().clickitem('bylink', dataoper.readxml('sche', 0, u'add_link'))
        time.sleep(2) 
        #选择开始时间
        WebDriverHelp().clickitem('bylid', dataoper.readxml('sche', 0, 'start_hour'))
        WebDriverHelp().selectvalue('byid', dataoper.readxml('sche', 0, 'start_hour'),
                                    dataoper.readxml('sche', 0, u'select_start_hour'))
        time.sleep(1)
        #选择结束时间
        WebDriverHelp().clickitem('bylid', dataoper.readxml('sche', 0, 'end_hour'))
        WebDriverHelp().selectvalue('byid', dataoper.readxml('sche', 0, 'end_hour'),
                                    dataoper.readxml('sche', 0, u'select_end_hour'))
        time.sleep(1) 
        #输入标题
        WebDriverHelp().inputvalue('byname', dataoper.readxml('sche', 0, 'title'),
                                   dataoper.readxml('sche', 0, 'title_name'))
        time.sleep(1) 
        #保存
        WebDriverHelp().clickitem('bycss', dataoper.readxml('sche', 0, 'save'))
        time.sleep(2) 
        #退出
        QT_Operations().logout()
        time.sleep(3) 
        
    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器
       
if __name__ == "__main__":   
    unittest.main()
