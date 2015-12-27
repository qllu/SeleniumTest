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

class SendMessage(unittest.TestCase):

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
        msg_name = "msg test2"
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-message']/a/div")
        driver.click("byxpath", "//div[@id='smart_main_menu_part']/span/span/a")
        driver.input("byname", "title", msg_name)
        driver.input("byid", "data_editor_id", "this is a message")
        # 添加收件人
        driver.input("byname", "keyword_CGID", "u2")
        driver.click("byxpath", u"//input[@value='用户搜索']")
        time.sleep(1)
        driver.click("byid", "btn_add_CID[]")
        # 设置更改/删除的许可
        driver.click("byid", "operator-set2")
        driver.click("byid", "btn_add_CID_o[]")
        time.sleep(1)
        # 提交
        driver.click("bycss", "input.margin")
        # 进入详细
        try:
            time.sleep(2)
            driver.click("bylink", msg_name)
            msg_detail_url = driver.currenturl()
        except NoSuchElementException as msg:
            print msg, "Can not add message."
            assert False

    def test2_confirm_message(self):
        Operations().login(u2_name, u2_pwd)
        driver.open(domain, "g")
        driver.click("byxpath", "//span[@id='appmenu-message']/a/div")
        time.sleep(2)
        driver.click("bylink", msg_name)
        driver.click("byxpath", "//small/div/span/a")
        time.sleep(1)
        # 验证
        if driver.is_element_present("bycss", ".lineone>td>img") is False:
            print "Maintainer is not checked."
            assert False

    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # 清除数据
        try:
            Operations().login(u1_name, u1_pwd)
            driver.geturl(msg_detail_url)
            time.sleep(2)
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
