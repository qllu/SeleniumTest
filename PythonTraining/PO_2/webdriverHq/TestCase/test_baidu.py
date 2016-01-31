#coding:utf-8


# from MyPage.basetestcase import BaseTestCase
# from MyPage.baidu import  BaiduPage
# from MyPage.homePage import  HomePage
# from model import Model
# from ddt import  ddt,data,unpack
import  unittest
from MyPage.basetestcase import BaseTestCase
from MyPage.baidu import  BingPage
from MyPage.homePage import  HomePage
# from model import Model
# from ddt import  ddt,data,unpack


# @ddt
class baiduPage(BaseTestCase, BingPage, HomePage):

	def test_search(self):
		self.search("hello")

	# @data(*Model.DataHelper().readExcels())
	# @unpack
	# def testLogin_001(self,username,password,context_expxcted):
	# 	'''测试：百度登录失败的N种情况'''
	# 	self.doLogin(username,password)
	# 	self.assertEqual(context_expxcted,self.getLoginErrorDiv())
    #
	# def testLogin_002(self):
	# 	'''测试：百度登录成功的情况'''
	# 	# db=Model.DataHelper()
	# 	# self.login(db.getXmlUser('login','username'),db.getXmlUser('login','password'))
	# 	self.login("", "")
	# 	self.assertEqual(db.getXmlUser('login','niCheng'),self.getNiCheng())

if __name__=='__main__':
	unittest.main(verbosity=2)
