# coding=utf-8
"""
Created on 2015年12月23日
1.変更/削除の許可を設定したメッセージが送信されること
2.宛先の詳細画面で変更/削除の許可欄にチェックが入っていること
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

class EditMessage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver, dataoper, u1_name, u1_pwd, u2_name, u2_pwd
        domain = "qatest01"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")
        dataoper = DataReader('USER_INFO.xml')
        u1_name = dataoper.readxml('u1', 0, 'username')
        u1_pwd = dataoper.readxml('u1', 0, 'password')
        u2_name = dataoper.readxml('u2', 0, 'username')
        u2_pwd = dataoper.readxml('u2', 0, 'password')

    def test1_change_recipients(self):
        global msg_detail_url, msg_name
        Operations().login(u1_name, u1_pwd)
        # send message
        msg_name = "msg test2"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-message']/a/div")
        driver.click("byxpath", "//div[@id='smart_main_menu_part']/span/span/a")
        driver.input("byname", "title", msg_name)
        driver.input("byid", "data_editor_id", "this is a message")
        # add recipients
        driver.input("byname", "keyword_CGID", "u2")
        driver.click("byxpath", u"//input[@value='用户搜索']")
        driver.wait(2)
        driver.click("byid", "btn_add_CID[]")
        # submit
        driver.click("bycss", "input.margin")
        # go to detail page
        driver.wait(3)
        driver.click("bylink", msg_name)
        msg_detail_url = driver.currenturl()
        # edit
        driver.click("byxpath", "//div[@id='main_menu_part']/span[2]/span/a")
        driver.select("byid", "selectbox_selected_users_sUID[]", "u2")
        driver.click("byid", "btn_rmv_CID[]")
        driver.wait(2)
        # add recipients
        driver.input("byname", "keyword_CGID", "u3")
        driver.click("byxpath", u"//input[@value='用户搜索']")
        driver.wait(2)
        driver.click("byid", "btn_add_CID[]")
        # change
        driver.click("bycss", "input.margin")
        # confirm
        if driver.is_element_present("bylink", "u3") is False:
            print "Recipients has not been added."
            assert False

    def test2_confirm_message(self):
        Operations().login(u2_name, u2_pwd)
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-message']/a/div")
        driver.wait(3)
        # confirm message is not exist
        if driver.is_element_present("bylink", msg_name) is True:
            print "Message cannot be deleted."
            assert False

    def test3_change_message(self):
        Operations().login(u1_name, u1_pwd)
        driver.geturl(msg_detail_url)
        driver.wait(2)
        driver.click("byxpath", "//div[@id='main_menu_part']/span/span/a")
        driver.clear("byid", "data_editor_id")
        driver.input("byid", "data_editor_id", "new content")
        # change
        driver.click("bycss", "input.margin")
        driver.wait(2)
        # confirm
        content = driver.gettext("byclass", "format_contents")
        self.assertEqual(content, "new content")

    def test4_delete_message(self):
        Operations().login(u1_name, u1_pwd)
        driver.geturl(msg_detail_url)
        driver.wait(3)
        driver.click("byid", "lnk_delete")
        # delete message from recipients
        driver.click("byid", "checkbox_id")
        driver.click("byid", "msgbox_btn_yes")

    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # 清除数据
        # try:
        #     Operations().login(u1_name, u1_pwd)
        #     driver.geturl(msg_detail_url)
        #     driver.wait(3)
        #     driver.click("byid", "lnk_delete")
        #     # 同时从收件人的文件夹中删除
        #     driver.click("byid", "checkbox_id")
        #     driver.click("byid", "msgbox_btn_yes")
        # except Exception as msg:
        #     print msg, "Message data has not been removed."
        # finally:
        driver.close()


if __name__ == "__main__":
    unittest.main()
