#coding=utf-8
'''
Created on 2015年10月12日

@author: LYE
'''

import xml.dom.minidom
import time,unittest
import sys,os
sys.path.append("..")
sys.path.append(os.getcwd()+"/src/")
from CommonFunction.DataReader import DataOperations
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp


#导入需要的公共函数类
class testcases_add_normalsche(unittest.TestCase):
    '''
    登录检测，更换用户登录
    '''
    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("fcn")#打开浏览器，并打开forest

    def test_add_normalsche(self):

        #读取测试数据     
        dataoper=DataOperations('QT_Add_normalSche.xml')

        #登录用户
        QT_Operations().login(dataoper.readxml('sche', 0, 'username'),dataoper.readxml('sche', 0, 'password'))

        #进入Garoon
        grn_url = "https://qatest01.cybozu.cn/g/"
        WebDriverHelp().geturl(grn_url)
        time.sleep(2) 
        #点击用户下拉菜单
        WebDriverHelp().clickitem('byid', dataoper.readxml('sche', 0, 'item'))
               
        checkpoint1 = WebDriverHelp().gettext('bycss',dataoper.readxml('sche', 0,'checkpoint'))
        value1 = dataoper.readxml('sche', 0, 'value')        
        self.assertEqual(checkpoint1,value1)         

        #点击日程登录菜单
        WebDriverHelp().clickitem('bycss', dataoper.readxml('sche', 0, 'sche_icon'))
        time.sleep(2) 

        #点击登录链接
        WebDriverHelp().clickitem('bylink', dataoper.readxml('sche', 0, u'add_link'))
        time.sleep(2) 
        #选择开始时间
        WebDriverHelp().clickitem('bylid', dataoper.readxml('sche', 0, u'start_hour'))        
        WebDriverHelp().selectvalue('byid', dataoper.readxml('sche', 0, 'start_hour'), dataoper.readxml('sche', 0, u'select_start_hour'))
        time.sleep(1)
        #选择结束时间
        WebDriverHelp().clickitem('bylid', dataoper.readxml('sche', 0, u'end_hour')) 
        WebDriverHelp().selectvalue('byid', dataoper.readxml('sche', 0, 'end_hour'), dataoper.readxml('sche', 0, u'select_end_hour'))
        time.sleep(1) 
        #输入标题
        WebDriverHelp().inputvalue('byname', dataoper.readxml('sche', 0, 'title'), dataoper.readxml('sche', 0, 'title_name'))
        time.sleep(1) 
        #选择用户
        #select = Select(driver.find_element_by_id(dataoper.readxml('sche', 0, u'select_CID[]'))
        #select.select_by_visible_text('u2')
        #WebDriverHelp().clickitem('bycss', dataoper.readxml('sche', 0, 'adduser'))
        #time.sleep(1) 
        #设为非公开
        WebDriverHelp().clickitem('bylid', dataoper.readxml('sche', 0, u'2')) 
        time.sleep(1) 
        #保存
        WebDriverHelp().clickitem('bycss', dataoper.readxml('sche', 0, 'save'))
        time.sleep(2) 
        
    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器
       
if __name__ == "__main__":   
    unittest.main()
