# coding=utf-8
"""
Created on 2015年12月05日
1.HTMLポートレットが追加されること
2.ポートレットをD&Dで配置できること
3.システムポータルが作成されること
@author: QLLU
"""
# 导入需要的公共函数类
import time
import unittest
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class CreatePortlet(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_add_html_portlet(self):
        global detail_url, dataoper, portal_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('admin', 0, 'username'),
                              dataoper.readxml('admin', 0, 'password'))
        driver.wait(3)
        # 进入追加HTML组件页面
        html_portlet_name = "html portlet test"
        driver.open(domain, "sys_app")
        driver.click("byid", "portal")
        portal_url = driver.currenturl()
        driver.wait(3)
        driver.click("byid", "portal/system/html_portlet_list")
        driver.click("byxpath", "//div[@id='main_menu_part']/span/span/a")
        driver.input("byid", "portletName-label-line-value-def", html_portlet_name)
        content = "<table class='top_title'> <tr><td><strong>cybozu</strong></td></tr>"
        driver.input("byid", "data_editor_id", content)
        driver.wait(3)
        driver.click("bycss", "input.margin")
        driver.click("bylink", html_portlet_name)
        detail_url = driver.currenturl()
        driver.click("byxpath", "//div[@id='main_menu_part']/span[3]/span/a")
        if driver.is_element_present("bycss", ".top_title>tbody>tr>td") is False:
            assert False

    def test2_add_public_portal(self):
        global portal_detail_url, new_portal_url
        # 添加门户
        portal_name = "portal test"
        driver.geturl(portal_url)
        driver.wait(3)
        driver.click("byid", "portal/system/list")
        driver.click("byxpath", "//div[@id='main_menu_part']/span/span/a")
        driver.input("byid", "portalName-label-line-value-def", portal_name)
        driver.wait(2)
        driver.click("bycss", "input.margin")
        driver.click("bylink", portal_name)
        # 打开门户详细画面，设置为公开
        portal_detail_url = driver.currenturl()
        driver.wait(3)
        driver.click("byxpath", "//span[@id='open_button_portal']/div/a")
        driver.wait(3)
        driver.click("byid", "msgbox_btn_yes")
        # 首页确认是否显示
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-portal']/a/div")
        driver.click("bylink", portal_name)
        driver.wait(2)
        get_portal_name = driver.gettext("bylink", portal_name)
        new_portal_url = driver.currenturl()
        self.assertEqual(get_portal_name, portal_name)

    def test3_drag_and_drop_portlet(self):
        # 拖拽添加组件
        driver.geturl(portal_detail_url)
        driver.wait(3)
        # driver.max_window()
        driver.drag_and_drop("#draggable_portlet_parts_p8>span", "#top")
        driver.wait(5)
        driver.is_element_present("byxpath", ".//*[@id='top']/div/li/div")
        driver.wait(3)
        driver.click("byxpath", "//*[@id='top']/div/li/div/table/tbody/tr[1]/td[2]/span/div/a")
        driver.wait(3)
        driver.geturl(new_portal_url)
        driver.wait(3)
        driver.is_element_present("bycss", ".portlet_title_grn>a")

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            driver.geturl(detail_url)
            driver.click("byxpath", "//div[@id='main_menu_part']/span[2]/span/a")
            driver.click("bycss", "input.margin")
            driver.geturl(portal_detail_url)
            driver.click("bycss", "#delete_portal")
            driver.click("bycss", "#msgbox_btn_yes")
        except Exception as msg:
            print msg, "Test data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
