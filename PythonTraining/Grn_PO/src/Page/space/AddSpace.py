#coding:utf-8
import sys
import os

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from CommonFunction import WebDriver
from CommonFunction import PageObject

class AddSpace(WebDriver.WebDriver, PageObject.PageObject):
    space_name_loc = (By.ID, "name-label-line-value-def")
    keyword_input_loc = (By.NAME, "keyword_CGID")
    search_loc = (By.XPATH, "//*[@name='keyword_CGID']/following-sibling::input")
    add_user_loc = (By.ID, "btn_add_CID[]")
    public_loc = (By.ID, "isPublic1")
    not_public_loc = (By.ID, "isPublic2")
    save_loc = (By.ID, "buttonSubmit")

    def test_add_space(self):
        self.find_element(*self.space_name_loc)













