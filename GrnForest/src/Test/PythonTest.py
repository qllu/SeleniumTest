# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time


class myclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test1(self):
        global NEW_URL
        url = "https://www.sogou.com/"
        print "start test1"
        self.driver.get(url)
        time.sleep(3)
        NEW_URL = self.driver.current_url
        print "current_url:", NEW_URL
        try:
            self.driver.find_element_by_xpath(".//*[@id='wrap']/div[3]/span").is_displayed()
        except NoSuchElementException:
            print "没有这个元素"

    def test2(self):
        print "start test2"
        self.driver.get(NEW_URL)
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='wrap']/div[3]/span").is_displayed()

        """
        try:
            self.driver.find_element_by_xpath(".//*[@id='wrap']/div[3]/span").is_displayed()
        except:
            print "未找到元素"
        else:
            print "元素存在"
        """

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
