#coding=utf-8
'''
Created on 2015年8月12日

@author: QLLU
'''
# from lib2to3.pgen2.driver import Driver
import time
import unittest
# import xml.dom.minidom

from TestCases.ParseXml import ParseXml

#导入需要的公共函数类
class ReadXml(unittest.TestCase): 
       
    def test(self):           
        #读取测试数据     
        dataoper=ParseXml('QT_loginGrn.xml')
              
        readname = dataoper.readxml('login', 1, 'username')                
        readpwd = dataoper.readxml('login', 1, 'password')   
        print 'readname:' + readname 
        print 'reapwd:' + readpwd           


       
if __name__ == "__main__":   
    unittest.main()