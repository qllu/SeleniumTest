# coding=utf-8
"""
Created on 2015年10月14日
1.予定のファイル添付が許可される
@author: QLLU
"""
# 导入需要的公共函数类
import time, unittest, sys, os
from selenium.common.exceptions import NoSuchElementException
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class AllowAttacheFiles(unittest.TestCase):

    def setUp(self):
        global domain
        domain = "qatest01"
        WebDriver("open", "firefox", "local").open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_allow_attache_files(self):
        dataoper = DataReader('QT_Sche_add_facility_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)

        # 进入日程安排系统后台
        WebDriver().open(domain, "sys_app")
        time.sleep(1)
        WebDriver().click("byid", "schedule")
        WebDriver().click("byid", "schedule/system/common_set")

        # 判断上传附件是否开启
        switch = WebDriver().is_selected("byid", "allow_file_attachment")
        if switch is False:
            WebDriver().click("byid", "allow_file_attachment")
            WebDriver().click("bycss", "input.margin")

        sche_url = WebDriver().testurl("qatest01") + "/g/schedule/index.csp?"
        WebDriver().geturl(sche_url)
        WebDriver().click("bycss", "span.menu_item > a")
        time.sleep(2)
        upfile = os.path.abspath('../Attachement/cybozu.gif')
        WebDriver().input("byid", "file_upload_", upfile)
        WebDriver().click("byid", "schedule_submit_button")
        time.sleep(2)
        if WebDriver().is_element_present("bycss", "tt > a > img") is False:
            print "上传失败"

    def tearDown(self):
        # 清空数据
        try:
            WebDriver().click("byxpath", "//span[2]/span/a")
            WebDriver().click("bycss", "input.margin")
        except NoSuchElementException as msg:
            print msg
        else:
            print "sche数据已清空"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
