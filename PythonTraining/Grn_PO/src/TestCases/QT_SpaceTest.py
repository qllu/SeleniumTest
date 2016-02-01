#coding=utf-8
import time
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.BaseTestCase import BaseTestCase
from Page.space.AddSpace import AddSpace
from Page.space.Index import Index
from Page.space.AddCategory import AddCategory

class SpaceTest(BaseTestCase, Index, AddCategory, AddSpace):


    def tearDown(self):
        self.logout()

    def test_001_add_system_category(self):
        self.login(self.admin_name, self.admin_pwd)
        self.open_sys_app()
        self.open_sys_space()
        self.add_sys_space_category("hello")
        self.delete_sys_space_category("hello")

    def test_002_add_pub_space(self):
        self.login(self.u1_name, self.u1_pwd)
        self.open_grn()
        self.open_space()
        self.create_space()
        self.add_space("testspace", "u2")
        time.sleep(3)


