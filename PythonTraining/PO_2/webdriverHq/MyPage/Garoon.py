#coding:utf-8
import os
import sys

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from selenium.webdriver.common.by import  By
from MyCommon.BasePage import  BasePage


class Garoon(BasePage):
	uname_loc = (By.NAME, "username")
	pwd_loc = (By.NAME, "password")
	login_loc = (By.CLASS_NAME, "login-button")

	def dologin(self, uname, pwd):
		self.find_element(*self.uname_loc).send_keys(uname)
		self.find_element(*self.pwd_loc).send_keys(pwd)
		self.find_element(*self.login_loc).click()



	"""
	def inputUsername(self, uname):
		self.find_element(*self.uname_loc).send_keys(uname)

	def inputPassword(self, pwd):
		self.find_element(*self.pwd_loc).send_keys(pwd)

	def clickLogin(self):
		self.find_element(*self.pwd_loc).click()

	def dologin(self, uname, pwd):
		time.sleep(2)
		self.inputUsername(uname)
		self.inputPassword(pwd)
		self.clickLogin()
		time.sleep(5)
	"""

	# def click(self):
	# 	self.wait()
	# 	self.find_element(*self.click_loc).click()
    #
	# def getUserTextField(self,username):
	# 	self.wait()
	# 	self.find_element(*self.userName_loc).send_keys(username)
    #
	# def getPasswordField(self,password):
	# 	self.wait()
	# 	self.find_element(*self.password_loc).send_keys(password)
    #
	# def getSubmitButton(self):
	# 	self.wait()
	# 	self.find_element(*self.clickButton_loc).click()
    #
	# def getLoginErrorDiv(self):
	# 	self.wait()
	# 	return self.find_element(*self.error_loc).text
    #
	# def login(self,username,password):
	# 	self.doLogin(username,password)
	# 	return HomePage(self.driver)
    #
	# def doLogin(self,username,password):
	# 	self.click()
	# 	self.getUserTextField(username)
	# 	self.getPasswordField(password)
	# 	self.getSubmitButton()





