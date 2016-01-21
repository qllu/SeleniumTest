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

class Cabinet(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver, dataoper, u1_name, u1_pwd, admin_name, admin_pwd
        domain = "qllu"
        driver = WebDriver("open","firefox","local")
        driver.open(domain, "slash")
        dataoper = DataReader('USER_INFO.xml')
        u1_name = dataoper.readxml('u1', 0, 'username')
        u1_pwd = dataoper.readxml('u1', 0, 'password')
        admin_name = dataoper.readxml('admin', 1, 'username')
        admin_pwd = dataoper.readxml('admin', 1, 'password')

    def test1_add_folder(self):
        # add cabinet folder
        global folder_detail_url, folder_name
        folder_name = "folder test1"
        Operations().login(admin_name, admin_pwd)
        driver.open(domain, "sys_app")
        driver.click("byid", "cabinet")
        driver.click("byid", "cabinet/system/folder_list")
        driver.wait(3)
        driver.click("bycss", "span.nowrap-grn > a")
        driver.wait(2)
        driver.input("byid", "folderName-label-line-value-def", folder_name)
        driver.click("byid", "enable_copy_access")
        driver.click("byid", "enable_copy_notification")
        driver.wait(3)
        # save
        driver.click("bycss", "input.margin")
        # go to detail page
        driver.click("bylink", folder_name)
        driver.click("byxpath", "//div[@id='main_menu_part']/span[2]/span/a")
        folder_detail_url = driver.currenturl()

    def test2_add_file(self):
        # add file
        upfile = os.path.abspath("../Attachement/test3.xls")
        Operations().login(admin_name, admin_pwd)
        driver.open(domain, "g")
        driver.click("bycss", "div.icon-appMenu-cabinet.appmenu-item-icon")
        driver.click("bylink", folder_name)
        driver.wait(2)
        driver.click("bycss", "span.menu_item > span.nowrap-grn > a")
        driver.input("byid", "file_upload_", upfile)
        driver.input("byxpath", ".//*[@id='fileTable']/tbody/tr[2]/td[6]/input", "upfile")
        driver.wait(5)
        driver.click("bycss", "input.margin")
        # confirm


    def test3_update_file(self):
        pass


    def tearDown(self):
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # remove data
        try:
            Operations().login(admin_name, admin_pwd)
            driver.geturl(folder_detail_url)
            driver.wait(2)
            driver.click("byxpath", "//div[@id='main_menu_part']/span[3]/span/a")
            driver.click("bycss", "input.margin")

        except Exception as msg:
            print msg, "Test data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
