# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.60.2.11/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
        count = 1
        msg_name = "msg"
        driver.get(self.base_url + "/grn/index.csp?")
        driver.find_element_by_name("_account").clear()
        driver.find_element_by_name("_account").send_keys("x1")
        driver.find_element_by_name("login-submit").click()
        driver.find_element_by_css_selector("div.icon-appMenu-message.appmenu-item-icon").click()
        while count <= 50:
            driver.find_element_by_link_text(u"发送站内信").click()
            driver.find_element_by_name("title").clear()
            driver.find_element_by_name("title").send_keys(msg_name + str(count))
            select = Select(driver.find_element_by_id("select_CID[]"))
            select.select_by_visible_text("x2")
            driver.find_element_by_id("btn_add_CID[]").click()
            driver.find_element_by_css_selector("input.margin").click()
            count = count + 1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
