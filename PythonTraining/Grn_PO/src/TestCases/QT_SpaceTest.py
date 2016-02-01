#coding=utf-8
import time
import sys
import os
import unittest
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from CommonFunction.BaseTestCase import BaseTestCase
from Page.space.ConfigSpace import ConfigSpace
from Page.space.Index import Index
from Page.space.ConfigCategory import ConfigCategory

class SpaceTest(BaseTestCase, Index, ConfigCategory, ConfigSpace):

    def tearDown(self):
        self.logout()

    def test_001_add_system_category(self):
        try:
            self.login(self.admin_name, self.admin_pwd)
            self.open_sys_app()
            self.click_sys_space_link()
            self.action_add_sys_space_category("test category")
            self.action_open_category_detail("test category")
            self.action_delete_sys_space_category()
        except (Exception, NoSuchElementException) as e:
            print e

    def test_002_add_pub_space(self):
        try:
            self.login(self.u1_name, self.u1_pwd)
            self.open_grn()
            self.click_space_icon()
            self.click_create_space_link()
            self.action_add_space("testspace", "u2", "private")
        except (Exception, NoSuchElementException) as e:
            print e

if __name__ == "__main__":
    unittest.main()


