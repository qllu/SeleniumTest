# coding=utf-8
"""
Created on 2015年12月23日
1.宛先が変更されること
2.宛先から外されたユーザーはメッセージが削除されていること
@author: QLLU
"""
import time, unittest, sys, os
from selenium.common.exceptions import NoSuchElementException

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver

class SendMessage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver, dataoper, u1_name, u1_pwd, u2_name, u2_pwd
        domain = "temp"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")
        dataoper = DataReader('USER_INFO.xml')
        u1_name = dataoper.readxml('u1', 0, 'username')
        u1_pwd = dataoper.readxml('u1', 0, 'password')
        u2_name = dataoper.readxml('u2', 0, 'username')
        u2_pwd = dataoper.readxml('u2', 0, 'password')

    def test1_send_message(self):
        global msg_detail_url, msg_name
        Operations().login("x1", "")
        # send message
        count = 1
        msg_name = "msg"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-message']/a/div")
        while count <= 50:
            driver.click("byxpath", "//div[@id='smart_main_menu_part']/span/span/a")
            driver.input("byname", "title", msg_name + str(count))
            driver.input("byid", "data_editor_id", "this is a message")
            # add recipients
            driver.input("byname", "keyword_CGID", "x2")
            driver.click("byxpath", u"//input[@value='用户搜索']")
            time.sleep(1)
            driver.click("byid", "btn_add_CID[]")
            # set maintainer
            driver.click("byid", "operator-set2")
            driver.click("byid", "btn_add_CID_o[]")
            time.sleep(1)
            # submit
            driver.click("bycss", "input.margin")
            count = count + 1

    def tearDown(self):
        # Operations().logout()
        driver.close()


if __name__ == "__main__":
    unittest.main()
