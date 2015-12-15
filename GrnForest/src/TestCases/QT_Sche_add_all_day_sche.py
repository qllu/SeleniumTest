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

class AddAppointments(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain
        domain = "qatest01"
        WebDriver("open","firefox","local").open(domain, "slash")

    def test1_add_appointments_with_users_facility(self):
        global dataoper, sche_detail_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        # 添加整日预定
        sche_name = "banner sche test"
        WebDriver().open(domain, "g")
        WebDriver().click("byxpath", "//span[@id='appmenu-schedule']/a/div")
        WebDriver().click("byxpath", "//div[@id='smart_main_menu_part']/span/a")
        WebDriver().click("bycss", "span.tab_text_noimage > a")
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
        sche_time = WebDriver().gettext("byclass", "mLeft15")
        print "output:", sche_time
        self.assertEqual(sche_time, u"00:00～23:59（全天）")

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
            WebDriver().click("bycss", "input.margin")
        except Exception as msg:
            print msg, "数据不能正常清除"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()
