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
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")

    def test1_add_repeat_appointment(self):
        global dataoper, sche_detail_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        lang = Operations().get_language()
        # print "lang:", lang
        # 添加整日预定
        sche_name = "repeat sche test"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-schedule']/a/div")
        # driver.findby("byxpath", "//span[@id='appmenu-schedule']/a/div").click()
        driver.click("byxpath", "//div[@id='smart_main_menu_part']/span/a")
        # 选择重复预定
        driver.click("byid", "tab-repeat-schedule")
        driver.click("byid", "week")
        # 输入时间
        # driver.click("byname", "wday")
        if lang == "CH":
            driver.select("byname", "wday", u"星期三")
        elif lang == "EN":
            driver.select("byname", "wday", "Wednesday")
        elif lang == "JP":
            driver.select("byname", "wday", u"水曜日")
        # driver.click("bycss", "option[value=\"3\"]")
        driver.click("byid", "time_selector")
        driver.click("byid", "time9")
        if lang == "CH":
            driver.click("bylink", u"关闭")
        elif lang == "EN":
            driver.click("bylink", u"Close")
        elif lang == "JP":
            driver.click("bylink", u"閉じる")
        driver.input("byname", "title", sche_name)

        # 检索用户并添加
        driver.wait(2)
        driver.input("byname", "keyword_CGID", "u2")
        driver.wait(2)
        driver.click("byid", "searchbox-submit-users")
        driver.wait(2)
        driver.click("bycss", "span.aButtonText-grn")
        # 检索设备并添加
        driver.wait(2)
        driver.input("byid", "facility_search_text", "test")
        driver.wait(2)
        driver.click("byid", "searchbox-submit-facilities")
        driver.wait(2)
        if lang == "CH":
            driver.click("byxpath", "//span[text()='添加']")
        else:
            driver.click("byxpath", ".//*[@id='schedule/repeat_add']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/div/div[1]/span/a")
        # 保存
        driver.click("byid", "schedule_submit_button")
        driver.wait(3)
        sche_detail_url = driver.currenturl()
        # 验证日期、时间、参加者、设备
        wday = driver.gettext("byxpath", ".//*[@id='body']/div[3]/div/div/table/tbody/tr[2]/td")
        # print "wday:", wday
        if lang == "CH":
            self.assertTrue(u"星期三" in wday)
        elif lang == "EN":
            self.assertTrue("Wednesday" in wday)
        elif lang == "JP":
            self.assertTrue(u"水曜日" in wday)

        sche_time = driver.gettext("bycss", "span.schedule_text_noticeable_grn")
        # print "time:", sche_time
        if lang == "CH" or lang == "JP":
            self.assertTrue(u"09:00 ～ 10:00" in sche_time)
        else:
            self.assertTrue("09:00  -  10:00" in sche_time)
        user = driver.gettext("bylink", "u2")
        self.assertEqual(user, "u2")
        facility = driver.gettext("bylink", "test")
        self.assertEqual(facility, "test")

    @classmethod
    def tearDownClass(self):
        try:
            # 清空预定
            # Operations().login(dataoper.readxml('u1', 0, 'username'),
            #                   dataoper.readxml('u1', 0, 'password'))
            driver.geturl(sche_detail_url)
            driver.wait(3)
            driver.click("byxpath", "//span[2]/span/a")
            # 删除全部参加者
            driver.click("byid", "1")
            # 删除全部预定
            driver.click("byid", "5")
            driver.click("bycss", "input.margin")
        except Exception as msg:
            print msg, "Data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
