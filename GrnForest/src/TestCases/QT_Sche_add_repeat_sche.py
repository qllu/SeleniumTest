# coding=utf-8
"""
Created on 2015年12月14日
1.指定した繰り返し条件で繰り返し予定が登録されること
2.参加者に予定の共有者が含まれていること
3.施設欄に施設が含まれていること
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

class AddRepeatAppointments(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain
        domain = "qatest01"
        WebDriver("open","firefox","local").open(domain, "slash")

    def test1_add_repeat_appointment(self):
        global dataoper, sche_detail_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        lang = Operations().get_language()
        print "lang:", lang
        # 添加整日预定
        sche_name = "repeat sche test"
        WebDriver().open(domain, "g")
        WebDriver().click("byxpath", "//span[@id='appmenu-schedule']/a/div")
        # WebDriver().findby("byxpath", "//span[@id='appmenu-schedule']/a/div").click()
        WebDriver().click("byxpath", "//div[@id='smart_main_menu_part']/span/a")
        # 选择重复预定
        WebDriver().click("byid", "tab-repeat-schedule")
        WebDriver().click("byid", "week")
        # 输入时间
        # WebDriver().click("byname", "wday")
        if lang == "CH":
            WebDriver().select("byname", "wday", u"星期三")
        elif lang == "EN":
            WebDriver().select("byname", "wday", "Wednesday")
        elif lang == "JP":
            WebDriver().select("byname", "wday", u"水曜日")
        # WebDriver().click("bycss", "option[value=\"3\"]")
        WebDriver().click("byid", "time_selector")
        WebDriver().click("byid", "time9")
        if lang == "CH":
            WebDriver().click("bylink", u"关闭")
        elif lang == "EN":
            WebDriver().click("bylink", u"Close")
        elif lang == "JP":
            WebDriver().click("bylink", u"閉じる")
        WebDriver().input("byname", "title", sche_name)

        # 检索用户并添加
        time.sleep(1)
        WebDriver().input("byname", "keyword_CGID", "u2")
        time.sleep(1)
        WebDriver().click("byid", "searchbox-submit-users")
        time.sleep(1)
        WebDriver().click("bycss", "span.aButtonText-grn")
        # 检索设备并添加
        time.sleep(1)
        WebDriver().input("byid", "facility_search_text", "test")
        time.sleep(1)
        WebDriver().click("byid", "searchbox-submit-facilities")
        time.sleep(1)
        if lang == "CH":
            WebDriver().click("byxpath", "//span[text()='添加']")
        else:
            WebDriver().click("byxpath", ".//*[@id='schedule/repeat_add']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/div/div[1]/span/a")
        # 保存
        WebDriver().click("byid", "schedule_submit_button")
        time.sleep(2)
        sche_detail_url = WebDriver().currenturl()
        # 验证日期、时间、参加者、设备
        wday = WebDriver().gettext("byxpath", ".//*[@id='body']/div[3]/div/div/table/tbody/tr[2]/td")
        # print "wday:", wday
        if lang == "CH":
            self.assertTrue(u"星期三" in wday)
        elif lang == "EN":
            self.assertTrue("Wednesday" in wday)
        elif lang == "JP":
            self.assertTrue(u"水曜日" in wday)

        sche_time = WebDriver().gettext("bycss", "span.schedule_text_noticeable_grn")
        # print "time:", sche_time
        if lang == "CH" or lang == "JP":
            self.assertTrue(u"09:00 ～ 10:00" in sche_time)
        else:
            self.assertTrue("09:00  -  10:00" in sche_time)
        user = WebDriver().gettext("bylink", "u2")
        self.assertEqual(user, "u2")
        facility = WebDriver().gettext("bylink", "test")
        self.assertEqual(facility, "test")

    @classmethod
    def tearDownClass(self):
        try:
            # 清空预定
            # Operations().login(dataoper.readxml('u1', 0, 'username'),
            #                   dataoper.readxml('u1', 0, 'password'))
            WebDriver().geturl(sche_detail_url)
            time.sleep(2)
            WebDriver().click("byxpath", "//span[2]/span/a")
            # 删除全部参加者
            WebDriver().click("byid", "1")
            # 删除全部预定
            WebDriver().click("byid", "5")
            WebDriver().click("bycss", "input.margin")
        except Exception as msg:
            print msg, "预定不能删除"
        else:
            print "预定已清除"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
