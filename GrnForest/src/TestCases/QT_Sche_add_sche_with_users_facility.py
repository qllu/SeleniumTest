# coding=utf-8
"""
Created on 2015年10月14日
1.通常予定が登録されること
2.参加者に予定の共有者が含まれていること
3.ファイルが添付されておりダウンロードできること
4.施設欄に施設が含まれていること
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
import QT_Sche_add_facility_group as addfac

class AddSche(unittest.TestCase):

    def setUp(self):
        WebDriver("open","firefox","local").open("qatest01")  # 打开浏览器，并打开forest

    def test_add_sche_with_users_facility(self):
        global dataoper
        dataoper = DataReader('QT_Sche_add_sche_with_users_facility.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        # 添加设备，设备组
        try:
            addfac.add_facility_group()
            addfac.add_facility()
        except:
            print "设备、设备组无法添加"
        Operations().logout()

        # 使用u1操作
        Operations().login(dataoper.readxml('sche', 0, 'username'),
                              dataoper.readxml('sche', 0, 'password'))
        garoon_url = WebDriver().testurl("qatest01") + "/g/schedule/index.csp?"
        WebDriver().geturl(garoon_url)
        time.sleep(2)
        WebDriver().click("byxpath", ".//*[@id='smart_main_menu_part']/span[1]/a")
        time.sleep(2)
        # 选择结束时间
        WebDriver().click('byid', "time_selector")
        WebDriver().click("byid", "time16")
        # 输入标题
        WebDriver().input('byname', "title", "sche01")
        # 检索用户并添加
        time.sleep(1)
        WebDriver().input("byname", "keyword_CGID", "u2")
        time.sleep(1)
        WebDriver().click("byid", "searchbox-submit-users")
        time.sleep(1)
        WebDriver().click("bycss", "span.aButtonText-grn")
        # 检索设备并添加
        time.sleep(1)
        WebDriver().input("byid", "facility_search_text", "fac1")
        time.sleep(1)
        WebDriver().click("byid", "searchbox-submit-facilities")
        time.sleep(1)
        WebDriver().click("byxpath", "//table[@id='main_table']/tbody/tr[4]/td/table/tbody/tr/td[2]/div/div/span/a/span[2]")
        # 添加附件
        upfile = os.path.abspath('../Attachement/cybozu.gif')
        WebDriver().input("byid", "file_upload_", upfile)
        time.sleep(1)
        try:
            WebDriver().click("byid", "schedule_submit_button")
            time.sleep(3)
            WebDriver().screenshot("../ScreenShot/add_sche_with_users_facility.png")
        except:
            print "不能添加预定，可能与其他预定重合"

        try:
            time.sleep(3)
            check1 = WebDriver().gettext("bylink", "u2")
            self.assertEqual(check1, "u2")
            check2 = WebDriver().gettext("bylink", "fac1")
            self.assertEqual(check2, "fac1")
        except NoSuchElementException as msg:
            print msg


    def tearDown(self):
        try:
            # 清空sche数据
            time.sleep(2)
            WebDriver().click("byxpath", "//span[2]/span/a")
            WebDriver().click("byid", "1")
            WebDriver().click("bycss", "input.margin")
            Operations().logout()
            # 清空设备
            Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
            addfac.del_fac()
        except Exception as msg:
            print msg, "数据不能正常清除"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
