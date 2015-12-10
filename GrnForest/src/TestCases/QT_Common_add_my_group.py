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


class AddMyGroup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        WebDriver("open", "firefox", "local").open("qatest01")  # 打开浏览器，并打开forest
        # filelog = "../Log/AddMyGroup.log"
        # WebDriver().getlog(filelog)

    def test1_add_my_group(self):
        global detail_url

        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        time.sleep(2)
        # language = "CH"
        # Operations().select_language(language)
        # 进入我的组的设置
        url = WebDriver().testurl("qatest01") + "/g/personal/common_list.csp?id=user"
        WebDriver().geturl(url)
        time.sleep(2)
        WebDriver().click("byid", "personal/user/mygroup_list")
        WebDriver().click("byid", "personal_mygroup_add")
        WebDriver().input("byname", "name", "my group")
        WebDriver().input("byid", "textarea_id", "this is a comment")
        WebDriver().click("byid", "mygroup_add_submit")
        # 进入详情页面
        WebDriver().click("byxpath", "//td[@id='view_part']/span/span/a")
        time.sleep(2)
        detail_url = WebDriver().currenturl()

        name = WebDriver().gettext("byxpath", "//div[3]/table/tbody/tr/td")
        comment = WebDriver().gettext("bycss", "pre.format_contents")
        self.assertEqual(name, "my group")
        self.assertEqual(comment, "this is a comment")


    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().geturl(detail_url)
            WebDriver().click("byid", "lnk_delete")
            WebDriver().click("byid", "msgbox_btn_yes")
        except Exception as msg:
            print msg, "数据不能正常清除"
        else:
            print "数据已清除"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
