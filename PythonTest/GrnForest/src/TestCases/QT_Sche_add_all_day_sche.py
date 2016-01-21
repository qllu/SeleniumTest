# coding=utf-8
"""
Created on 2015年12月14日
1.期間予定が登録されること
2.参加者に予定の共有者が含まれていること
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

class AddAllDayAppointment(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")

    def test1_add_all_day_appointment(self):
        global dataoper, sche_detail_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        # 添加整日预定
        sche_name = "banner sche test"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-schedule']/a/div")
        # driver.findby("byxpath", "//span[@id='appmenu-schedule']/a/div").click()
        driver.click("byxpath", "//div[@id='smart_main_menu_part']/span/a")
        # 选择整日预定
        driver.click("bycss", "span.tab_text_noimage > a")
        driver.input("byname", "title", sche_name)
        # 检索用户并添加
        driver.wait(2)
        driver.input("byname", "keyword_CGID", "u2")
        driver.wait(2)
        driver.click("byid", "searchbox-submit-users")
        driver.wait(2)
        driver.click("bycss", "span.aButtonText-grn")
        driver.click("byid", "schedule_submit_button")
        driver.wait(3)
        sche_detail_url = driver.currenturl()
        sche_time = driver.gettext("bycss", "span.schedule_text_noticeable_grn")
        # print "output:", sche_time
        self.assertTrue( u"00:00～23:59" in sche_time)
        # self.assertIn(u"00:00～23:59", sche_time)
        user = driver.gettext("bylink", "u2")
        self.assertEqual(user, "u2")

    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        try:
            # 清空预定
            Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
            driver.geturl(sche_detail_url)
            driver.wait(3)
            driver.click("byxpath", "//span[2]/span/a")
            # 删除全部参加者
            driver.click("byid", "1")
            driver.click("bycss", "input.margin")
        except Exception as msg:
            print msg, "Data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
