#coding:utf-8

from selenium import  webdriver
from appium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By
import  time


class PageObject(object):
	def __init__(self, driver):
		# self.driver = driver
		self.driver = driver

	# find element by different type
	def find_element(self, *loc):
		try:
			return  self.driver.find_element(*loc)
		except (NoSuchElementException, KeyError, ValueError, Exception), e:
			print 'Error details:%s'%(e.args[0])

	# find elements by different type
	def find_elements(self, *loc):
		try:
			return  self.driver.find_elements(*loc)
		except (NoSuchElementException, KeyError, ValueError, Exception), e:
			print 'Error details:%s'%(e.args[0])

	def wait(self, sec):
		self.driver.implicitly_wait(sec)

	def get_current_url(self):
		return self.driver.current_url

	def refresh(self):
		self.driver.refresh()