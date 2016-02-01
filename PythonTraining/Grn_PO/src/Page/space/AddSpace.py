#coding:utf-8
import sys
import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from CommonFunction.PageObject import PageObject

class AddSpace(PageObject):
    space_name_loc = (By.ID, "name-label-line-value-def")
    keyword_input_loc = (By.NAME, "keyword_CGID")
    search_loc = (By.XPATH, "//*[@name='keyword_CGID']/following-sibling::input")
    add_user_loc = (By.ID, "btn_add_CID[]")
    public_loc = (By.ID, "isPublic1")
    not_public_loc = (By.ID, "isPublic2")
    save_loc = (By.ID, "buttonSubmit")

    def add_space(self, spacename, uname):
        self.find_element(*self.space_name_loc).send_keys(spacename)
        self.find_element(*self.keyword_input_loc).send_keys(uname)
        self.find_element(*self.search_loc).click()
        self.find_element(*self.add_user_loc).click()
        self.find_element(*self.public_loc).click()
        self.find_element(*self.save_loc).click()















