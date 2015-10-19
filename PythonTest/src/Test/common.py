#coding=utf-8
from selenium import webdriver

class common(object):
    def setup(self):
        global driver
        driver = webdriver.Firefox()

    def teardown(self):
        driver.close()

    def geturl(self,url):
        driver.get(url)

    def currenturl(self):
        return driver.current_url



