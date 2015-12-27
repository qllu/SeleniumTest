# coding=utf-8
"""
Created on 2015年10月14日
1.フォローが書き込めること
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

class AddFllow(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")

    def test1_add_follow(self):
        global dataoper, sche_detail_url
        dataoper = DataReader('USER_INFO.xml')
        Operations().login(dataoper.readxml('u1', 0, 'username'),
                              dataoper.readxml('u1', 0, 'password'))
        # 添加预定
        sche_name = "sche follow test"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-schedule']/a/div")
        driver.click("byxpath", ".//*[@id='smart_main_menu_part']/span[1]/a")
        # 选择普通预定，输入标题，选择时间
        driver.input("byname", "title", sche_name)
        driver.click("byid", "time_selector")
        driver.click("byid", "time9")
        driver.click("bylink", u"关闭")
        # 检索用户并添加
        time.sleep(1)
        driver.input("byname", "keyword_CGID", "u2")
        time.sleep(1)
        driver.click("byid", "searchbox-submit-users")
        time.sleep(1)
        driver.click("bycss", "span.aButtonText-grn")
        driver.click("byid", "schedule_submit_button")
        time.sleep(2)
        sche_detail_url = driver.currenturl()
        # 输入comment
        driver.input("byid", "textarea_id", "comment1")
        driver.click("byclass", "button_min_width2_grn")
        time.sleep(2)
        # 验证
        comment = driver.gettext("byxpath", "//pre[text()='comment1']")
        self.assertEqual(comment, "comment1")

    @classmethod
    def tearDownClass(self):
        # 清除数据
        try:
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
