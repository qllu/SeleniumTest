# coding=utf-8
'''
Created on 2015年10月14日
1.スペースのメンバーが作成したスペースを閲覧できること
2.スペースの参加者以外も作成されたスペースを閲覧できること
@author: QLLU
'''
# 导入需要的公共函数类
import time
import unittest
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from Grn_PO.src.CommonFunction.DataReader import DataReader
from Grn_PO.src.CommonFunction.Operations import Operations
from Grn_PO.src.CommonFunction.WebDriver import WebDriver
from Grn_PO.src.CommonFunction.BaseTestCase import BaseTestCase
from Grn_PO.src.Page.space import AddSpace
from Grn_PO.src.Page.space import Common

class CreatePublicSpace(BaseTestCase):
    '''
    Add Space
    '''
    @classmethod
    def setUpClass(self):
        # global domain, driver, u1_name, u1_pwd
        # domain = "qatest01"
        # driver = WebDriver("open", "firefox", "local")
        # driver.open(domain, "slash")
        # dataoper = DataReader('USER_INFO.xml')
        # u1_name = dataoper.readxml('u1', 0, 'username')
        # u1_pwd = dataoper.readxml('u1', 0, 'password')
        # u2_name = dataoper.readxml('u2', 0, 'username')
        # u2_pwd = dataoper.readxml('u2', 0, 'password')
        pass

    def test_Add_Space(self):
        # time.sleep(2)
        # Operations().login(u1_name, u1_pwd)
        # driver.open(domain, "g")
        # self.Common.OpenSpace()
        pass

    @classmethod
    def tearDownClass(self):
        # close browser
        # driver.close()
        pass

    def tearDown(self):
        # logout
        # Operations().logout()
        pass


if __name__ == "__main__":
    unittest.main()
