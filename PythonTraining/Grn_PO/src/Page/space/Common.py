#coding:utf-8
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from Grn_PO.src.CommonFunction.PageObject import PageObject

class Common(PageObject):
    space_icon_loc = (By.CSS_SELECTOR, "div.icon-appMenu-space.appmenu-item-icon")
    creat_link_loc = (By.CSS_SELECTOR, ".icon-add-grn")

    def OpenSpace(self):
        sleep(2)
        self.find_element(*self.space_icon_loc).click()

    def CreateSpace(self):
        sleep(2)
        self.find_element(*self.creat_link_loc).click()
