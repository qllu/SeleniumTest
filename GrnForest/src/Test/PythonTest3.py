# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import unittest
import time

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
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("username-:0-text").clear()
        driver.find_element_by_id("username-:0-text").send_keys("u1")
        driver.find_element_by_id("password-:1-text").clear()
        driver.find_element_by_id("password-:1-text").send_keys("cybozu1")
        driver.find_element_by_css_selector("input.login-button").click()
        time.sleep(2)
        driver.get("https://qatest01.cybozu.cn/g/schedule/index.csp?")
        time.sleep(2)
        driver.find_element_by_link_text(u"周").click()
        time.sleep(2)
        element = driver.find_element_by_xpath("//form/div[4]/div[1]/table/tbody/tr/td[3]/div/div[12]")
        target = driver.find_element_by_xpath("//div[4]/div[1]/table/tbody/tr/td[3]/div/div[4]")
        actionChains = ActionChains(driver)
        actionChains.drag_and_drop(element, target).perform()

        time.sleep(2)
        driver.find_element_by_css_selector("span.buttonSpacePlus-grn").click()


        driver.find_element_by_css_selector("span").click()
        driver.find_element_by_id("com-header-logout-link").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

