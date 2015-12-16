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
        WebDriver().click("byid", "time_selector")
        WebDriver().click("byid", "time9")
        WebDriver().click("bylink", u"关闭")
        WebDriver().input("byname", "title", sche_name)

        # 检索用户并添加
        time.sleep(1)
        WebDriver().input("byname", "keyword_CGID", "u2")
        time.sleep(1)
        WebDriver().click("byid", "searchbox-submit-users")
        time.sleep(1)
        WebDriver().click("bycss", "span.aButtonText-grn")
        WebDriver().click("byid", "schedule_submit_button")
        time.sleep(2)
        sche_detail_url = WebDriver().currenturl()
        # sche_time = WebDriver().gettext("bycss", "span.schedule_text_noticeable_grn")
        # print "output:", sche_time
        # self.assertTrue( u"00:00～23:59" in sche_time)
        # user = WebDriver().gettext("bylink", "u2")
        # self.assertEqual(user, "u2")

    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        try:
            # 清空预定
            Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
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
