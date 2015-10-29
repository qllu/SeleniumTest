# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest, time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qatest01.cybozu.cn/"

    def test1(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        # driver.find_element_by_name("username").send_keys("Administrator")
        driver.find_element_by_css_selector("[name=username]").send_keys("Administrator")
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("qatest01")
        time.sleep(1)
        driver.find_element_by_class_name("login-button").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
