# coding=utf-8
"""
Created on 2015年12月23日
1.ファイルを添付したメッセージが送信されること
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

class SendAndReciveMessage(unittest.TestCase):

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

    def test1_send_message(self):
        global msg_detail_url, msg_name
        Operations().login(u1_name, u1_pwd)
        # 发送站内信
        msg_name = "msg test"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-message']/a/div")
        driver.click("byxpath", "//div[@id='smart_main_menu_part']/span/span/a")
        driver.input("byname", "title", msg_name)
        driver.input("byid", "data_editor_id", "this is a message")
        # 添加收件人
        driver.input("byname", "keyword_CGID", "u2")
        driver.click("byxpath", u"//input[@value='用户搜索']")
        driver.wait(2)
        driver.click("byid", "btn_add_CID[]")
        driver.wait(2)
        # 上传附件
        upfile = os.path.abspath('../Attachement/test3.xls')
        driver.input("byid", "file_upload_", upfile)
        driver.wait(3)
        driver.click("bycss", "input.margin")
        # 进入详细
        driver.wait(3)
        driver.click("bylink", msg_name)
        msg_detail_url = driver.currenturl()
        # 验证
        filename = driver.gettext("bylink", "test3.xls")
        self.assertEqual(filename, "test3.xls")

    def test2_add_comment(self):
        Operations().login(u1_name, u1_pwd)
        driver.geturl(msg_detail_url)
        driver.input("byid", "data_editor_id", "comment1")
        upfile = os.path.abspath('../Attachement/cybozu.gif')
        driver.input("byid", "file_upload_message_comment", upfile)
        driver.click("byclass", "button_min_width2_grn")
        driver.wait(3)
        # 验证
        if driver.is_element_present("bycss", ".vAlignTop-grn>tt>a>img") is True:
            comment = driver.gettext("byxpath", "//pre[text()='comment1']")
            self.assertEqual(comment, "comment1")
        else:
            assert False

    def test3_confirm_notification_and_message(self):
        Operations().login(u2_name, u2_pwd)
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-notification']/a")
        driver.click("byxpath", "//td[@id='tree_part']/div[2]/span/a")
        driver.wait(3)
        if driver.is_element_present("bylink", msg_name) is True:
            driver.click("bylink", msg_name)
            filename = driver.gettext("bylink", "test3.xls")
            self.assertEqual(filename, "test3.xls")
        else:
            assert False

    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # 清除数据
        try:
            Operations().login(u1_name, u1_pwd)
            driver.geturl(msg_detail_url)
            driver.wait(3)
            driver.click("byid", "lnk_delete")
            # 同时从收件人的文件夹中删除
            driver.click("byid", "checkbox_id")
            driver.click("byid", "msgbox_btn_yes")
        except Exception as msg:
            print msg, "Message data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
