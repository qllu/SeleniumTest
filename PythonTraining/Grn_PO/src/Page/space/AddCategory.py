#coding:utf-8
import sys
import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from CommonFunction.PageObject import PageObject

class AddCategory(PageObject):
    sys_category_loc = (By.ID, "space/system/category_list")
    sys_add_category_loc = (By.XPATH, ".//*[@id='main_menu_part']/span[1]/span/a")
    sys_category_name_loc = (By.ID, "name-label-line-value-def")
    sys_category_memo_loc = (By.ID, "memo")
    sys_category_save_loc = (By.CSS_SELECTOR, "input.margin")
    sys_category_detail_loc = (By.XPATH, ".//*[@id='view_part']/div[1]/div/span[2]/span/a")
    sys_category_delete_loc = (By.XPATH, ".//*[@id='main_menu_part']/span[3]/span/a")
    sys_category_delete_yes_loc = (By.XPATH, ".//*[@onclick='submit(this.form)']")

    def add_sys_space_category(self, category_name):
        self.wait(5)
        self.find_element(*self.sys_category_loc).click()
        self.action_sys_add_category()
        self.action_sys_category_name_textbox(category_name)
        self.find_element(*self.sys_category_save_loc).click()

    def delete_sys_space_category(self, category_name):
        self.wait(5)
        self.find_element(By.LINK_TEXT, category_name).click()
        self.find_element(*self.sys_category_detail_loc).click()
        self.find_element(*self.sys_category_delete_loc).click()
        self.find_element(*self.sys_category_delete_yes_loc).click()

    def action_sys_add_category(self):
        self.find_element(*self.sys_add_category_loc).click()

    def action_sys_category_name_textbox(self, category_name):
        self.find_element(*self.sys_category_name_loc).send_keys(category_name)












