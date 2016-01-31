#coding=utf-8
import time
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.PageObject import PageObject
from CommonFunction.BaseTestCase import BaseTestCase
from Page.space import AddSpace
from Page.space import Index

class SpaceTest(BaseTestCase):

    def test_add_space(self):
        self.setUp()
        self.tearDown()

