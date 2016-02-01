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
    # ******  system application list location   ***********
    sys_space_loc = (By.ID, "space")

    # ******  space location   ***********
    space_icon_loc = (By.CSS_SELECTOR, "div.icon-appMenu-space.appmenu-item-icon")
    creat_link_loc = (By.CSS_SELECTOR, ".icon-add-grn")

    # ******  system application list action  ******
    def click_sys_space_link(self):
        self.wait(5)
        self.find_element(*self.sys_space_loc).click()

    # ******   space action   *******
    def click_space_icon(self):
        self.wait(5)
        self.find_element(*self.space_icon_loc).click()

    def click_create_space_link(self):
        self.wait(5)
        self.find_element(*self.creat_link_loc).click()

