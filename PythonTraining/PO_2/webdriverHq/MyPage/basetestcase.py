#coding:utf-8

import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		# self.driver.maximize_window()
		self.driver.get('https://qatest01.cybozu.cn/g/')
		self.driver.implicitly_wait(30)

	def tearDown(self):
		self.driver.quit()

