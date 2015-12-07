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
        WebDriver("open", "firefox", "local").open("qatest01")  # 打开浏览器，并打开forest

    def test1_change_to_japanese(self):
        global setting_url
        dataoper = DataReader('QT_Common_add_my_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 进入语言修改页面
        setting_url = WebDriver().testurl("qatest01") + "/settings/account"
        garoon_url = WebDriver().testurl("qatest01") + "/g/"
        WebDriver().geturl(setting_url)
        time.sleep(2)
        WebDriver().click("byid", ":1")
        time.sleep(1)
        # :3 日语，:4 英语，:5 中文
        WebDriver().click("byid", ":3")
        time.sleep(1)
        WebDriver().click("byid", "form-submit-button-slash")
        WebDriver().geturl(garoon_url)
        time.sleep(2)
        name = WebDriver().gettext("bycss", "#appmenu-portal>a>div>nobr")
        self.assertEqual(name, u"ポータル")

    def test2_change_to_english(self):
        pass

    def test3_change_to_chinese(self):
        pass


    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().geturl(setting_url)

        except Exception as msg:
            print msg, "数据不能还原"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
