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
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest
        # filelog = "../Log/AddMyGroup.log"
        # driver.getlog(filelog)

    def test1_add_my_group(self):
        global detail_url, group_url

        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        driver.wait(2)
        # language = "CH"
        # Operations().select_language(language)
        # 进入我的组的设置
        driver.open(domain, "person_set")
        driver.wait(2)
        driver.click("byid", "user")
        driver.click("byid", "personal/user/mygroup_list")
        driver.click("byid", "personal_mygroup_add")
        driver.input("byname", "name", "my group")
        driver.input("byid", "textarea_id", "this is a comment")
        driver.click("byid", "mygroup_add_submit")
        group_url = driver.currenturl()
        # 进入详情页面
        driver.click("byxpath", "//td[@id='view_part']/span/span/a")
        driver.wait(2)
        detail_url = driver.currenturl()
        name = driver.gettext("byxpath", "//div[3]/table/tbody/tr/td")
        comment = driver.gettext("bycss", "pre.format_contents")
        self.assertEqual(name, "my group")
        self.assertEqual(comment, "this is a comment")

    def test2_add_user_to_group(self):
        driver.geturl(group_url)
        driver.click("byid", "mygroup_user_add_link")
        driver.input("byname", "search_text", "u2")
        driver.click("byid", "search_submit")
        driver.select("byname", "aid[]", "u2")
        driver.click("byname", "add")
        driver.click("byid", "user_select_submit")
        driver.wait(2)
        driver.geturl(detail_url)
        user = driver.gettext("bylink", "u2")
        self.assertEqual(user, "u2")

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            driver.geturl(detail_url)
            driver.click("byid", "lnk_delete")
            driver.click("byid", "msgbox_btn_yes")
        except Exception as msg:
            print msg, "Test data can not be removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
