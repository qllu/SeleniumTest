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
        global domain
        domain = "qatest01"
        WebDriver("open", "firefox", "local").open(domain, "slash")  # 打开浏览器，并打开forest
        # filelog = "../Log/AddMyGroup.log"
        # WebDriver().getlog(filelog)

    def test1_add_my_group(self):
        global detail_url, group_url

        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        time.sleep(2)
        # language = "CH"
        # Operations().select_language(language)
        # 进入我的组的设置
        WebDriver().open(domain, "person_set")
        time.sleep(2)
        WebDriver().click("byid", "user")
        WebDriver().click("byid", "personal/user/mygroup_list")
        WebDriver().click("byid", "personal_mygroup_add")
        WebDriver().input("byname", "name", "my group")
        WebDriver().input("byid", "textarea_id", "this is a comment")
        WebDriver().click("byid", "mygroup_add_submit")
        group_url = WebDriver().currenturl()
        # 进入详情页面
        WebDriver().click("byxpath", "//td[@id='view_part']/span/span/a")
        time.sleep(2)
        detail_url = WebDriver().currenturl()
        name = WebDriver().gettext("byxpath", "//div[3]/table/tbody/tr/td")
        comment = WebDriver().gettext("bycss", "pre.format_contents")
        self.assertEqual(name, "my group")
        self.assertEqual(comment, "this is a comment")

    def test2_add_user_to_group(self):
        WebDriver().geturl(group_url)
        WebDriver().click("byid", "mygroup_user_add_link")
        WebDriver().input("byname", "search_text", "u2")
        WebDriver().click("byid", "search_submit")
        WebDriver().select("byname", "aid[]", "u2")
        WebDriver().click("byname", "add")
        WebDriver().click("byid", "user_select_submit")
        time.sleep(2)
        WebDriver().geturl(detail_url)
        user = WebDriver().gettext("bylink", "u2")
        self.assertEqual(user, "u2")
        # if WebDriver().is_element_present("bylink", "u3") is True:
        #     print "pass"
        # else:
        #     print "fail"

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
