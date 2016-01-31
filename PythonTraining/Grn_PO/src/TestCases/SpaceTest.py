#coding=utf-8
import time
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.BaseTestCase import BaseTestCase
from Page.space.AddSpace import AddSpace
from Page.space.Index import Index

class SpaceTest(BaseTestCase, AddSpace, Index):
    def test_add_space(self):
        self.login(self.u1_name, self.u1_pwd)
        self.open_space()
        self.create_space()
        self.add_space("test")
        time.sleep(3)


