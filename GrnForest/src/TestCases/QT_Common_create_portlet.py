# coding=utf-8
"""
Created on 2015年10月14日
1.施設グループが追加されること
2.施設が追加されること
@author: QLLU
"""
# 导入需要的公共函数类
import time
import unittest
import sys
import os
import logging
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class CreatePortlet(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        WebDriver("open", "firefox", "local").open("qatest01")  # 打开浏览器，并打开forest

    def test1_creating_an_html_portlet(self):
        global detail_url
        dataoper = DataReader('QT_Common_create_portlet.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 进入追加HTML组件页面
        url = WebDriver().testurl("qatest01") + "/g/system/application_list.csp?app_id=portal"
        WebDriver().geturl(url)
        time.sleep(2)
        WebDriver().click("byid", "portal/system/html_portlet_list")
        WebDriver().click("byxpath", "//div[@id='main_menu_part']/span/span/a")
        WebDriver().input("byid", "portletName-label-line-value-def", "portlet test")
        content = "<table class='top_title'> <tr><td><strong>cybozu</strong></td></tr>"
        WebDriver().input("byid", "data_editor_id", content)
        WebDriver().click("bycss", "input.margin")
        WebDriver().click("bylink", "portlet test")
        detail_url = WebDriver().currenturl()
        WebDriver().click("byxpath", "//div[@id='main_menu_part']/span[3]/span/a")
        WebDriver().is_element_present("bycss", ".top_title>tbody>tr>td")


    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().geturl(detail_url)
            WebDriver().click("byxpath", "//div[@id='main_menu_part']/span[2]/span/a")
            WebDriver().click("bycss", "input.margin")
        except Exception as msg:
            print msg, "数据不能正常清除"
        else:
            print "数据已清除"
        finally:
            WebDriver().close()

if __name__ == "__main__":
    unittest.main()
