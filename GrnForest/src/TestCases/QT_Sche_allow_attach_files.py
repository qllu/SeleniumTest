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
        WebDriver("open", "firefox", "local").open("qatest01")  # 打开浏览器，并打开forest


    def test1_allow_attache_files(self):
        dataoper = DataReader('QT_Sche_add_facility_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        #确认是否可以上传附件
        sche_url = WebDriver().testurl("qatest01") + "/g/schedule/index.csp?"
        WebDriver().geturl(sche_url)
        WebDriver().click("bycss", "span.menu_item > a")

        try:
            WebDriver().is_element_present("byxpath", "//tr[9]/td/div/div")
        except:
            print "开关没有打开，正在打开开关..."
            # 进入日程安排系统后台
            garoon_url = WebDriver().testurl("qatest01") + "/g/system/application_list.csp?app_id="
            WebDriver().geturl(garoon_url)
            time.sleep(1)
            WebDriver().click("byid", "schedule")
            WebDriver().click("byid", "schedule/system/common_set")
            # 设置附件
            WebDriver().click("byid", "allow_file_attachment")
            WebDriver().click("bycss", "input.margin")
            WebDriver().geturl(sche_url)

        time.sleep(2)
        upfile = os.path.abspath('../Attachement/cybozu.gif')
        WebDriver().input("byid", "file_upload_", upfile)
        WebDriver().click("byid", "schedule_submit_button")
        time.sleep(2)

        try:
            WebDriver().is_element_present("bycss", "tt > a > img")
        except NoSuchElementException as msg:
            print msg
        else:
            print "附件上传成功，可正常显示"


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
