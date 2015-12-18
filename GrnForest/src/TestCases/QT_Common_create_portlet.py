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
        global domain
        domain = "qatest01"
        WebDriver("open", "firefox", "local").open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_add_html_portlet(self):
        global detail_url, dataoper, portal_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('admin', 0, 'username'),
                              dataoper.readxml('admin', 0, 'password'))
        time.sleep(2)
        # 进入追加HTML组件页面
        html_portlet_name = "html portlet test"
        WebDriver().open(domain, "sys_app")
        WebDriver().click("byid", "portal")
        portal_url = WebDriver().currenturl()
        time.sleep(2)
        WebDriver().click("byid", "portal/system/html_portlet_list")
        WebDriver().click("byxpath", "//div[@id='main_menu_part']/span/span/a")
        WebDriver().input("byid", "portletName-label-line-value-def", html_portlet_name)
        content = "<table class='top_title'> <tr><td><strong>cybozu</strong></td></tr>"
        WebDriver().input("byid", "data_editor_id", content)
        time.sleep(2)
        WebDriver().click("bycss", "input.margin")
        WebDriver().click("bylink", html_portlet_name)
        detail_url = WebDriver().currenturl()
        WebDriver().click("byxpath", "//div[@id='main_menu_part']/span[3]/span/a")
        WebDriver().is_element_present("bycss", ".top_title>tbody>tr>td")

    def test2_add_public_portal(self):
        global portal_detail_url, new_portal_url
        # 添加门户
        portal_name = "portal test"
        WebDriver().geturl(portal_url)
        time.sleep(2)
        WebDriver().click("byid", "portal/system/list")
        WebDriver().click("byxpath", "//div[@id='main_menu_part']/span/span/a")
        WebDriver().input("byid", "portalName-label-line-value-def", portal_name)
        time.sleep(1)
        WebDriver().click("bycss", "input.margin")
        WebDriver().click("bylink", portal_name)
        # 打开门户详细画面，设置为公开
        portal_detail_url = WebDriver().currenturl()
        time.sleep(2)
        WebDriver().click("byxpath", "//span[@id='open_button_portal']/div/a")
        time.sleep(2)
        WebDriver().click("byid", "msgbox_btn_yes")
        # 首页确认是否显示
        WebDriver().open(domain, "g")
        WebDriver().click("byxpath", "//span[@id='appmenu-portal']/a/div")
        WebDriver().click("bylink", portal_name)
        time.sleep(1)
        get_portal_name = WebDriver().gettext("bylink", portal_name)
        new_portal_url = WebDriver().currenturl()
        self.assertEqual(get_portal_name, portal_name)

    def test3_drag_and_drop_portlet(self):
        # 拖拽添加组件
        WebDriver().geturl(portal_detail_url)
        time.sleep(2)
        # WebDriver().max_window()
        WebDriver().drag_and_drop("#draggable_portlet_parts_p8>span", "#top")
        time.sleep(3)
        WebDriver().is_element_present("byxpath", ".//*[@id='top']/div/li/div")
        time.sleep(2)
        WebDriver().click("byxpath", "//*[@id='top']/div/li/div/table/tbody/tr[1]/td[2]/span/div/a")
        time.sleep(2)
        WebDriver().geturl(new_portal_url)
        time.sleep(2)
        WebDriver().is_element_present("bycss", ".portlet_title_grn>a")

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().geturl(detail_url)
            WebDriver().click("byxpath", "//div[@id='main_menu_part']/span[2]/span/a")
            WebDriver().click("bycss", "input.margin")
            WebDriver().geturl(portal_detail_url)
            WebDriver().click("bycss", "#delete_portal")
            WebDriver().click("bycss", "#msgbox_btn_yes")
        except Exception as msg:
            print msg, "数据不能正常清除"
        else:
            print "数据已清除"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
