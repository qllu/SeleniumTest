#coding:utf-8
import sys
import os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from CommonFunction.PageObject import PageObject

class Index(PageObject):
    space_icon_loc = (By.CSS_SELECTOR, "div.icon-appMenu-space.appmenu-item-icon")
    creat_link_loc = (By.CSS_SELECTOR, ".icon-add-grn")

    def open_space(self):
        sleep(2)
        self.find_element(*self.space_icon_loc).click()

    def create_space(self):
        sleep(2)
        self.find_element(*self.creat_link_loc).click()

