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
        driver.find_element_by_id("username-:0-text").send_keys("Administrator")
        driver.find_element_by_id("password-:1-text").clear()
        driver.find_element_by_id("password-:1-text").send_keys("qatest01")
        driver.find_element_by_css_selector("input.login-button").click()
        time.sleep(2)
        driver.get("https://qatest01.cybozu.cn/g/portal/system/view.csp?pid=3")
        time.sleep(2)
        source = driver.find_element_by_css_selector("#draggable_portlet_parts_p8>span")
        target = driver.find_element_by_css_selector("#top")
        # action = ActionChains(driver).click_and_hold(source).move_to_element(target)
        ActionChains(driver).drag_and_drop(source, target).perform()

        time.sleep(3)

    def tearDown(self):
        # self.driver.quit()
        pass

if __name__ == "__main__":
    unittest.main()

