#coding:utf-8

import unittest
import time
from selenium import webdriver
from CommonFunction.DataReader import DataReader

# this class contains setup/teardown, login/logout function
class BaseTestCase(unittest.TestCase):

	dataoper = DataReader('BASE_INFO.xml')
	admin_name = dataoper.readxml('admin', 0, 'username')
	admin_pwd = dataoper.readxml('admin', 0, 'password')
	u1_name = dataoper.readxml('u1', 0, 'username')
	u1_pwd = dataoper.readxml('u1', 0, 'password')
	u2_name = dataoper.readxml('u2', 0, 'username')
	u2_pwd = dataoper.readxml('u2', 0, 'password')
	domain = dataoper.readxml('url', 0, 'qatest01')

	@classmethod
	def setUpClass(cls):
		global driver

		cls.driver = webdriver.Firefox()
		# cls.driver.maximize_window()
		cls.driver.get(cls.domain)
		cls.driver.implicitly_wait(30)

		driver = cls.driver

	@classmethod
	def tearDownClass(cls):
		driver.quit()

	def login(self, uname, pwd):
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_name("username").clear()
		self.driver.find_element_by_name("username").send_keys(uname)
		self.driver.find_element_by_name("password").clear()
		self.driver.find_element_by_name("password").send_keys(pwd)
		self.driver.find_element_by_class_name("login-button").click()
		time.sleep(3)

	def logout(self):
		self.driver.get(self.domain + "/logout")

	def open_grn(self):
		self.driver.get(self.domain + "/g/")

	def open_sys_common(self):
		self.driver.get(self.domain + "/g/system/common_list.csp?")

	def open_sys_app(self):
		self.driver.get(self.domain + "/g/system/application_list.csp?app_id=")














