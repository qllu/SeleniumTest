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


    def test_001_add_system_category(self):

        self.login(self.admin_name, self.admin_pwd)
        self.open_sys_app()
        self.click_sys_space_link()
        self.action_add_sys_space_category("test07 category")
        self.action_open_category_detail("test07 category")
        self.action_delete_sys_space_category()


    def test_002_add_pub_space(self):

        self.login(self.u1_name, self.u1_pwd)
        self.open_grn()
        self.open_space()
        self.click_create_space_link()
        self.action_add_space("testspace", "u2")
        self.action_open_space_detail()
        self.action_delete_space()

    def test_aa(self):
        self.login(self.u1_name, self.u1_pwd)
        self.open_grn()
        self.open_space()
        self.select_space("testspace")



if __name__ == "__main__":
    unittest.main()


