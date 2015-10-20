# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest, time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qatest01.cybozu.cn/"


    def test1(self):   
        global current_url     
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("Administrator")
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("qatest01")
        time.sleep(1)
        driver.find_element_by_class_name("login-button").click()
        time.sleep(3)
        driver.get('https://qatest01.cybozu.cn/g/space/top.csp?spid=23')
        time.sleep(3)
        current_url = driver.current_url
        print 'current_url:', current_url
        
    def test2(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("u3")
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("cybozu1")
        time.sleep(1)
        driver.find_element_by_class_name("login-button").click()
        time.sleep(3)  
        print "open space by u3"  
        driver.get(current_url)
        time.sleep(3)
        try:
            driver.find_element_by_class_name('error_main_grn').is_displayed()
        except NotImplementedError:
            print "找不到错误页面"



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
