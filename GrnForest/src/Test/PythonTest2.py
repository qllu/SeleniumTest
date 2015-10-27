#!/usr/bin/env python
#encoding: utf-8

import time, unittest, sys, os

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver

dataoper = DataReader('QT_Space_add_share_todo.xml')
test1 = dataoper.readxml_attribute('space', 0, 'space_icon', 'desc')
test2 = dataoper.readxml('space', 0, 'creat_link')
time.sleep(2)
print "test1:", test1
print "test2:", test2




