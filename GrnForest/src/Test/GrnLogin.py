# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
        # self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
        # self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)

        self.driver.implicitly_wait(30)
        self.base_url = "https://qatest01.cybozu.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login?redirect=https%3A%2F%2Fqatest01.cybozu.cn%2F")
        time.sleep(2)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("Administrator")
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("qatest01")
        time.sleep(1)
        driver.find_element_by_class_name("login-button").click()
        time.sleep(3)
        driver.get('https://qatest01.cybozu.cn/g/')
        # time.sleep(3)
        # print "页面刷新"
        # driver.refresh()
        time.sleep(3)
        url = driver.current_url
        print 'url:', url
        driver.find_element_by_css_selector('span').click()
        time.sleep(1)

        uname = driver.find_element_by_css_selector("div > a").text
        try:
            self.assertEqual(u"Administrator", uname)
        except AssertionError, msg:
            print msg

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
