# coding=utf-8
"""
Created on 2015年12月23日
1.強制通知が設定されること
※カテゴリにメガネアイコンが表示される
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

class CreateCategory(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver, dataoper, u1_name, u1_pwd, admin_name, admin_pwd
        domain = "qatest01"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")
        dataoper = DataReader('USER_INFO.xml')
        u1_name = dataoper.readxml('u1', 0, 'username')
        u1_pwd = dataoper.readxml('u1', 0, 'password')
        admin_name = dataoper.readxml('admin', 0, 'username')
        admin_pwd = dataoper.readxml('admin', 0, 'password')

    def test1_create_category(self):
        global category_detail_url, cat_name
        Operations().login(admin_name, admin_pwd)
        cat_name = "category test1"
        # add bulletin category
        driver.open(domain, "sys_app")
        driver.click("byid", "bulletin")
        driver.click("byid", "bulletin/system/category_list")
        driver.click("byid", "bulletin_category_add")
        driver.input("byid", "categoryName-label-line-value-def", cat_name)
        driver.click("byid", "bulletin_category_form_submit")
        # go to detail page
        driver.click("bylink", cat_name)
        driver.click("byid", "bulletin_category_detail")
        category_detail_url = driver.currenturl()
        # confirm
        driver.wait(3)
        title = driver.gettext("byid", "bulletin_category_title")
        self.assertEqual(cat_name, title)

    def test2_edit_notification(self):
        # set notification on
        Operations().login(admin_name, admin_pwd)
        # driver.geturl(category_detail_url)
        driver.open(domain, "sys_app")
        driver.click("byid", "bulletin")
        driver.wait(2)
        driver.click("byid", "bulletin/system/notify_index")
        driver.click("bylink", cat_name)
        driver.click("bycss", "span.menu_item > span.nowrap-grn > a")
        driver.click("bycss", "span.m_small > span.nowrap-grn > a")
        # add role
        driver.click("byid", "activate-right-tab")
        driver.wait(3)
        driver.select("byname", "aid[]", "Everyone")
        driver.click("byname", "add")
        driver.click("byxpath", ".//*[@class='margin'][@type='button']")
        # confirm
        driver.open(domain, "g")
        driver.click("bycss", "div.icon-appMenu-bulletin.appmenu-item-icon")
        driver.wait(3)
        if driver.is_element_present("byclass", "icon_mark_subscribe_grn") is False:
            print "Notification icon is not display."
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
