# coding=utf-8
"""
Created on 2015年10月14日
1.通常予定が登録されること
2.参加者に予定の共有者が含まれていること
3.ファイルが添付されておりダウンロードできること
4.施設欄に施設が含まれていること
5.登録した予定が未確認の通知として存在すること
6.タイトル、日時、メモ、参加者、施設、添付ファイルなどの変更内容が反映されていること
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

class AddAppointments(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        WebDriver("open","firefox","local").open("qatest01", "slash")

    def test1_add_appointments_with_users_facility(self):
        global dataoper, sche_url
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
        WebDriver().click("byxpath", "//span[text()='添加']")
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

        sche_url = WebDriver().currenturl()
        time.sleep(3)
        # 验证用户、设备是否添加
        check1 = WebDriver().gettext("bylink", "u2")
        self.assertEqual(check1, "u2")
        check2 = WebDriver().gettext("bylink", "fac1")
        self.assertEqual(check2, "fac1")


    def test2_confirm_notifacation(self):
        # 验证未读通知是否存在
        Operations().login(dataoper.readxml('confirm', 0, 'username'),
                              dataoper.readxml('confirm', 0, 'password'))
        notifacation_url = WebDriver().testurl("qatest01") + "/g/notification/pending_list.csp?module_id="
        WebDriver().geturl(notifacation_url)
        time.sleep(2)
        check = WebDriver().gettext("bylink", "16:00 sche01")
        self.assertEqual(check, "16:00 sche01")

    def test3_change_appointments(self):
        # 修改预定
        Operations().login(dataoper.readxml('sche', 0, 'username'),
                              dataoper.readxml('sche', 0, 'password'))
        WebDriver().geturl(sche_url)
        time.sleep(2)
        WebDriver().click("byxpath", ".//*[@id='main_menu_part']/div[1]/span[1]/span/a")
        time.sleep(2)
        # 选择结束时间
        WebDriver().click('byid', "time_selector")
        WebDriver().click("byid", "time17")
        # 输入标题
        WebDriver().clear("byname", "title")
        WebDriver().input("byname", "title", "sche01 change")
        # 检索用户并添加
        time.sleep(1)
        WebDriver().input("byname", "keyword_CGID", "u3")
        time.sleep(1)
        WebDriver().click("byid", "searchbox-submit-users")
        time.sleep(1)
        WebDriver().click("bycss", "span.aButtonText-grn")
        # 去除设备
        time.sleep(1)
        WebDriver().click("byxpath", "//tr[4]/td/table/tbody/tr/td[2]/div/div[2]/span/a/span[2]")
        # 更换附件
        WebDriver().click("byname", "fids[]")
        upfile = os.path.abspath('../Attachement/test3.xls')
        WebDriver().input("byid", "file_upload_", upfile)
        time.sleep(1)
        WebDriver().input("byid", "textarea_id", "this is a comment")
        WebDriver().click("bycss", "#schedule_submit_button > span")
        time.sleep(3)
        # 验证标题、时间、用户、设备、附件、备注是否修改

        title = WebDriver().gettext("byclass", "schedule")
        self.assertEqual(title, "sche01 change")
        date = WebDriver().gettext("bycss", ".mLeft15")
        self.assertEqual(date, u"17:00 ～ 18:00")
        user = WebDriver().gettext("bylink", "u3")
        self.assertEqual(user, "u3")
        comment = WebDriver().gettext("byclass", "format_contents")
        self.assertEqual(comment, "this is a comment")
        attachment = WebDriver().gettext("bylink", "test3.xls")
        self.assertEqual(attachment, "test3.xls")
        # assertNotEquals，验证内容不存在
        facility = WebDriver().gettext("byxpath", ".//*[@id='body']/div[3]/div/div/table/tbody/tr[2]/td/div")
        self.assertNotEqual(facility, "fac1")


    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        try:
            # 清空sche数据
            Operations().login(dataoper.readxml('sche', 0, 'username'),
                              dataoper.readxml('sche', 0, 'password'))
            WebDriver().geturl(sche_url)
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
