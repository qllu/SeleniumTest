#coding:utf-8
import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By
from CommonFunction.BasePage import BasePage
from CommonFunction.BaseTestCase import BaseTestCase

class SystemApplicationList(BasePage, BaseTestCase):
    # ****************************
    def url_sys_app(self):
        pass
