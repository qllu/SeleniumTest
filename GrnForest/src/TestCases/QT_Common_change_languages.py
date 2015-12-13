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
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class ChangeLanguages(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain
        domain = "qatest01"
        WebDriver("open", "firefox", "local").open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_change_to_japanese(self):
        global lang_url, default_lang
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        time.sleep(2)
        # 进入语言修改页面
        lang_url = WebDriver().testurl(domain) + "/settings/account"
        WebDriver().geturl(lang_url)
        time.sleep(2)
        default_lang = Operations().get_language()
        WebDriver().click("byid", ":1")

        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":3")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().open(domain, "g")
        WebDriver().refresh()
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, u"ポータル"), "语言不能修改为日语"

    def test2_change_to_english(self):
        WebDriver().geturl(lang_url)
        time.sleep(2)
        WebDriver().click("byid", ":1")
        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":4")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().open(domain, "g")
        WebDriver().refresh()
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, "Portal"), "语言不能修改为英语"

    def test3_change_to_chinese(self):
        WebDriver().geturl(lang_url)
        time.sleep(2)
        WebDriver().click("byid", ":1")
        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":5")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().open(domain, "g")
        WebDriver().refresh()
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, u"门户"), "语言不能修改为中文"

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().geturl(lang_url)
            WebDriver().click("byid", ":1")
            WebDriver().click("byid", default_lang)
            WebDriver().click("byid", "form-submit-button-slash")
        except Exception as msg:
            print msg, "语言不能还原"
        else:
            print "语言已还原"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
