#coding:utf-8
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from CommonFunction.PageObject import PageObject

class SystemCommon(PageObject):
    pass

