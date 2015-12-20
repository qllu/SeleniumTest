#coding=utf-8
'''
Created on 2015年8月12日

QT_Operations 用来存放具体操作功能块，如登录，退出等

@author: QLLU
'''
import time
#import win32api
#import win32con
 
from WebDriver import WebDriver

class Operations(object):
    '''
    Grn相关操作
    '''
    def login(self,userName,passwd):
        '''
        从首页直接登录
        @param userName: 用户名
        @param passwd:密码
        @param type1:指示登录方式，1为从主页登录，2，从登录页登录
        '''

        WebDriver().click("byname", "username")
        time.sleep(3)
        WebDriver().clear('byname','username')
        WebDriver().input('byname','username',userName)
        time.sleep(1)
        WebDriver().clear('byname','password')
        WebDriver().input('byname','password',passwd)
        time.sleep(1)
        WebDriver().click("byclass", "login-button")
        time.sleep(2)
        # WebDriverFunction().geturl("https://qatest01.cybozu.cn")
        # time.sleep(2)

    def select_language(self, language):
        setting_url = WebDriver().testurl("qatest01") + "/settings/account"
        WebDriver().geturl(setting_url)
        # lang = WebDriver().gettext("byid", ":1")
        time.sleep(2)
        if (language == "JP"):
            WebDriver().click("byid", ":1")
            time.sleep(1)
            WebDriver().click("byid", ":3")

        elif (language == "EN"):
            WebDriver().click("byid", ":1")
            time.sleep(1)
            WebDriver().click("byid", ":4")

        elif (language == "CH"):
            WebDriver().click("byid", ":1")
            time.sleep(1)
            WebDriver().click("byid", ":5")
        time.sleep(2)
        WebDriver().click("byid", "form-submit-button-slash")
        time.sleep(2)
        WebDriver().refresh()

    def get_language(self):
        setting_url = WebDriver().testurl("qatest01") + "/settings/account"
        WebDriver().geturl(setting_url)
        time.sleep(2)
        lang = WebDriver().gettext("byid", ":1")
        # print "初始语言：", lang
        if lang == u"日本語":
            # lang_element = ":3"
            language = "JP"
            return language

        elif lang == "English (US)":
            # lang_element = ":4"
            language = "EN"
            return language
            # print "element0:", element
        elif lang == u"中文（简体）":
            # lang_element = ":5"
            language = "CH"
            return language
            # print "element0:", element


    def logout(self):
        '''
        退出登录
        '''
        logout_url = WebDriver().testurl("qatest01") + "/logout"
        WebDriver().geturl(logout_url)

        