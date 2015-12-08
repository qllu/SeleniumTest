# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import unittest
import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qatest01.cybozu.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        global element
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username-:0-text").clear()
        driver.find_element_by_id("username-:0-text").send_keys("u1")
        driver.find_element_by_id("password-:1-text").clear()
        driver.find_element_by_id("password-:1-text").send_keys("cybozu1")
        driver.find_element_by_css_selector("input.login-button").click()
        time.sleep(2)
        driver.get("https://qatest01.cybozu.cn/settings/account")
        time.sleep(2)
        driver.find_element_by_id(":1").click()
        time.sleep(1)
        lang = driver.find_element_by_id(":1").text
        print "初始语言:", lang
        if lang == u"日本語":
            element = ":3"
            print "element0:", element
        elif lang == "English (US)":
            element = ":4"
            print "element0:", element
        elif lang == u"中文（简体）":
            element = ":5"
            print "element0:", element
        print "element1:", element

        driver.find_element_by_id(":3").click()
        time.sleep(2)
        driver.find_element_by_id("form-submit-button-slash")
        time.sleep(2)
        driver.get("https://qatest01.cybozu.cn/g/")
        time.sleep(3)

    def tearDown(self):
        self.driver.get("https://qatest01.cybozu.cn/settings/account")
        print "element2:", element
        time.sleep(2)
        self.driver.find_element_by_id(":1").click()
        self.driver.find_element_by_id(element).click()
        self.driver.find_element_by_id("form-submit-button-slash")
        self.driver.get("https://qatest01.cybozu.cn/g")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

