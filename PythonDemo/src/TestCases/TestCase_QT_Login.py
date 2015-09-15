#coding=utf-8
'''
Created on 2015年8月12日

@author: QLLU
'''
# from lib2to3.pgen2.driver import Driver
import time
import unittest
# import xml.dom.minidom

from CommonFunction.DataOperations import DataOperations
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp


class testcases_login(unittest.TestCase):
    '''
    confirm login by different user
    '''
    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("grncn")     
       
    def testlogin(self): 
        
        #read test data     
        dataoper=DataOperations('TestCase_QT_Login.xml') 
        
        #设置起始节点为0，循环2次
        num = 0
        while num < 2:        
            #login
            QT_Operations().login(dataoper.readxml('login', num, 'username'),dataoper.readxml('login', num, 'password'))  
            #click user menu
            WebDriverHelp().clickitem('byid', dataoper.readxml('login', num, 'item'))
                   
            checkpoint1 = WebDriverHelp().gettext('bycss',dataoper.readxml('login', num,'checkpoint'))
            value1 = dataoper.readxml('login', num, 'value')        
            self.assertEqual(checkpoint1,value1) 
            #logout
            QT_Operations().logout()
            time.sleep(3)    
                        
            num = num + 1            

        
    def tearDown(self):
        WebDriverHelp().teardown()#close browser
       
if __name__ == "__main__":   
    unittest.main()