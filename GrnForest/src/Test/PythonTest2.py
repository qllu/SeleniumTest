#!/usr/bin/env python
#encoding: utf-8

import time, unittest, sys, os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp

class mytest(unittest.TestCase):
    def setUp(self):
        WebDriverHelp("open", "firefox", "local").setup("fdev")

    def test(self):
        pass

