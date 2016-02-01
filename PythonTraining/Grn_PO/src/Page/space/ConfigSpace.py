#coding:utf-8
import sys
import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from CommonFunction.PageObject import PageObject

class ConfigSpace(PageObject):
    # ******************************
    space_name_loc = (By.ID, "name-label-line-value-def")
    keyword_input_loc = (By.NAME, "keyword_CGID")
    search_loc = (By.XPATH, "//*[@name='keyword_CGID']/following-sibling::input")
    add_user_loc = (By.ID, "btn_add_CID[]")
    public_loc = (By.ID, "isPublic1")
    not_public_loc = (By.ID, "isPublic2")
    save_loc = (By.ID, "buttonSubmit")
    space_menu_loc = (By.ID, "space-operation")
    space_detail_loc = (By.XPATH, ".//*[@id='dialog']/ul/li[4]/a")
    # ********************************
    delete_space_loc = (By.ID, "space/delete")
    delete_yes_loc = (By.XPATH, ".//input[@type='submit']")


    def action_add_space(self, space_name, uname, stype="public"):
        self.find_element(*self.space_name_loc).send_keys(space_name)
        self.find_element(*self.keyword_input_loc).send_keys(uname)
        self.find_element(*self.search_loc).click()
        self.find_element(*self.add_user_loc).click()
        if (stype == "public"):
            self.find_element(*self.public_loc).click()
        elif (stype == "private"):
            self.find_element(*self.not_public_loc).click()
        self.find_element(*self.save_loc).click()

    def action_open_space_detail(self):
        self.find_element(*self.space_menu_loc).click()
        self.find_element(*self.space_detail_loc).click()

    def action_delete_space(self, space_name):
        self.find_element(*self.delete_space_loc).click()
        self.find_element(*self.delete_yes_loc).click()

















