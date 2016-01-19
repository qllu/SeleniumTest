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
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_allow_attache_files(self):
        dataoper = DataReader('QT_Sche_add_facility_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        driver.wait(3)

        # 进入日程安排系统后台
        driver.open(domain, "sys_app")
        driver.wait(2)
        driver.click("byid", "schedule")
        driver.click("byid", "schedule/system/common_set")

        # 判断上传附件是否开启
        switch = driver.is_selected("byid", "allow_file_attachment")
        if switch is False:
            driver.click("byid", "allow_file_attachment")
            driver.click("bycss", "input.margin")

        sche_url = driver.testurl("qatest01") + "/g/schedule/index.csp?"
        driver.geturl(sche_url)
        driver.click("bycss", "span.menu_item > a")
        driver.wait(3)
        upfile = os.path.abspath('../Attachement/cybozu.gif')
        driver.input("byid", "file_upload_", upfile)
        driver.click("byid", "schedule_submit_button")
        driver.wait(3)
        if driver.is_element_present("bycss", "tt > a > img") is False:
            print "Upload file failed."
            assert False

    def tearDown(self):
        # 清空数据
        try:
            driver.click("byxpath", "//span[2]/span/a")
            driver.click("bycss", "input.margin")
        except NoSuchElementException as msg:
            print msg, "Appointment data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
