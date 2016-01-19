# coding=utf-8
"""
Created on 2015年12月23日
1.ファイルを添付した掲示が作成できること
2.掲示が未確認の通知として存在すること
3.ファイルを添付したフォローを書き込めること
@author: QLLU
"""
import unittest, sys, os
import time
from selenium.common.exceptions import NoSuchElementException

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver

class PostTopic(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver, dataoper, u1_name, u1_pwd, admin_name, admin_pwd
        domain = "qatest01"
        driver = WebDriver("open","chrome","local")
        driver.open(domain, "slash")
        dataoper = DataReader('USER_INFO.xml')
        u1_name = dataoper.readxml('u1', 0, 'username')
        u1_pwd = dataoper.readxml('u1', 0, 'password')
        admin_name = dataoper.readxml('admin', 0, 'username')
        admin_pwd = dataoper.readxml('admin', 0, 'password')

    def test1_post_topic_with_attachement(self):
        global category_detail_url, cat_name, topic_detail_url, topic_name
        Operations().login(admin_name, admin_pwd)
        cat_name = "category test2"
        # add bulletin category
        driver.open(domain, "sys_app")
        driver.click("byid", "bulletin")
        driver.click("byid", "bulletin/system/category_list")
        driver.click("byid", "bulletin_category_add")
        driver.input("byid", "categoryName-label-line-value-def", cat_name)
        if driver.is_selected("byid", "enable_copy_access") is True:
            driver.click("byid", "enable_copy_access")
        if driver.is_selected("byid", "enable_copy_notification") is True:
            driver.click("byid", "enable_copy_notification")
        driver.click("byid", "bulletin_category_form_submit")
        # go to detail page
        driver.click("bylink", cat_name)
        driver.click("byid", "bulletin_category_detail")
        category_detail_url = driver.currenturl()
        # add topic
        topic_name = "topic test1"
        upfile = os.path.abspath('../Attachement/test3.xls')
        driver.open(domain, "g")
        driver.click("bycss", "div.icon-appMenu-bulletin.appmenu-item-icon")
        driver.click("bylink", cat_name)
        driver.wait(2)
        driver.click("byid", "bulletin_send")
        driver.wait(2)
        driver.input("byname", "title", topic_name)
        driver.input("byid", "data_editor_id", "this is content")
        driver.input("byid", "file_upload_", upfile)
        driver.wait(3)
        driver.click("bycss", "input.margin")
        # go to detail page
        driver.wait(2)
        driver.click("bylink", topic_name)
        topic_detail_url = driver.currenturl()
        # confirm
        if driver.is_element_present("bylink", "test3.xls") is False:
            print "Attachement is not exist."
            assert False

    def test2_confirm_notification(self):
        # edit notification
        Operations().login(u1_name, u1_pwd)
        driver.open(domain, "g")
        driver.click("bycss", "div.icon-appMenu-bulletin.appmenu-item-icon")
        driver.wait(3)
        driver.click("bylink", cat_name)
        driver.click("byid", "bulletin_set_subscribe")
        driver.wait(3)
        driver.click("byxpath", ".//*[@name='candidate_categories[]']/option[1]")
        driver.click("byname", "add")
        driver.click("byid", "bulletin_set_subscribe_submit")
        # go to notification page
        driver.wait(3)
        driver.click("bycss", "div.icon-appMenu-notification.appmenu-item-icon")
        driver.click("bycss", "div.tree_item > span.nowrap-grn > a")
        # confirm
        if driver.is_element_present("bylink", topic_name) is False:
            print "Notification is not exist."
            assert False

    def test3_add_comment(self):
        # add comment with attachement
        upfile = os.path.abspath('../Attachement/test3.xls')
        Operations().login(u1_name, u1_pwd)
        driver.open(domain, "g")
        driver.click("bycss", "div.icon-appMenu-bulletin.appmenu-item-icon")
        driver.wait(3)
        driver.click("bylink", cat_name)
        driver.wait(3)
        driver.click("bylink", topic_name)
        driver.wait(2)
        driver.input("byid", "data_editor_id", "comment1")
        driver.input("byid", "file_upload_article_comment", upfile)
        driver.wait(3)
        driver.click("byclass", "button_min_width2_grn")
        # confirm
        if driver.is_element_present("bylink", "test3.xls") is False:
            print "Attachement is not exist."
            assert False

    def test4_delete_topic(self):
        # delete topic
        Operations().login(admin_name, admin_pwd)
        driver.geturl(topic_detail_url)
        driver.wait(3)
        try:
            driver.click("byid", "lnk_delete")
            driver.click("byid", "msgbox_btn_yes")
        except:
            print "Topic cannot be deleted."
            assert False

    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # remove data
        try:
            Operations().login(admin_name, admin_pwd)
            driver.geturl(category_detail_url)
            driver.wait(3)
            driver.click("byxpath", "//div[@id='main_menu_part']/span[3]/span/a")
            driver.click("bycss", "input.margin")
        except Exception as msg:
            print msg, "Test data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
